import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



def pH2aH(pH):
    return 10 ** (-1 * pH)


def calc_fO2(aH_list, delta34S_H2S, k, gamma, delta, params):
    logfO2_list = []
    valid_pH_list = []
    invalid_aH = 1
    valid_flag = 0
    invalid_valid_pH = ()

    min_X_SUM_SO4 = 1
    max_X_SUM_SO4 = 0
    for aH in aH_list:
        A = (k['H2S'] * gamma['H2S']) / (gamma['HS'] * aH)
        B = k['HS'] * gamma['HS'] / (aH * gamma['S'])
        D = 1 / gamma['SO4']
        E = aH / (k['HSO4'] * gamma['HSO4'])
        F = params['mK'] * gamma['K']/ (k['KSO4'] * gamma['KSO4'])
        G = params['mNa'] * gamma['Na'] / (k['NaSO4'] * gamma['NaSO4'])
        H = params['mCa'] * gamma['Ca'] / (k['CaSO4'] * gamma['CaSO4'])

        C = ((delta['totalS'] - delta34S_H2S) * (1 + A * (1 + B)) - delta['HS'] * A - delta['S'] * A * B)  / ((delta['SO4'] - (delta['totalS'] - delta34S_H2S)) * (D + E + F + G + H))

        X_SUM_SO4 = C * (D + E + F + G + H) / (1 + A *(1 + B) + C * (D + E + F + G + H))
        min_X_SUM_SO4 = 0 if min(min_X_SUM_SO4, X_SUM_SO4) < 0 else min(min_X_SUM_SO4, X_SUM_SO4)
        max_X_SUM_SO4 = max(max_X_SUM_SO4, X_SUM_SO4)
        
        factor = k['SO4'] * aH ** 2  / gamma['H2S']
        try:
            logfO2 = math.log10(math.sqrt(C * factor))
            if valid_flag == 0:
                invalid_valid_pH = (-1 * np.log10(invalid_aH), -1 * np.log10(aH))
                valid_flag = 1
            logfO2_list.append(logfO2)
            valid_pH_list.append(-1 * math.log10(aH))
        except ValueError:
            invalid_aH = aH
    # print(round(min_X_SUM_SO4, 2), round(max_X_SUM_SO4, 2))
    return (logfO2_list, valid_pH_list, invalid_valid_pH)


def get_valid_pH_list(invalid_valid_pH, max_pH, delta34S_H2S, k, gamma, delta, params):
    has_solution = True
    if len(invalid_valid_pH) == 2:
        valid_pH_list = np.append(np.linspace(invalid_valid_pH[0], invalid_valid_pH[1], 1000), np.linspace(invalid_valid_pH[1], max_pH, 1000))
        valid_aH_list = list(map(pH2aH, valid_pH_list))
        logfO2_list, valid_pH_list, invalid_valid_pH = calc_fO2(valid_aH_list, delta34S_H2S, k, gamma, delta, params)
    else:
        has_solution = False
        logfO2_list, valid_pH_list = 0, 0
    return logfO2_list, valid_pH_list, invalid_valid_pH, has_solution


def main(T_c, delta_totalS, plot_species, delta_list, log_fo2_range, pH_range, default_ph_range, use_default_ph_range, figsize=(6, 7)):
    # params = {
    #     "mK": 10,
    #     "mNa": 10,
    #     "mCa":5
    # }
    params = {
        "mK": 1.5,
        "mNa": 1.5,
        "mCa": .01
    }

    ionic_strength = 3

    # set aH list
    if use_default_ph_range:
        min_pH = default_ph_range[0]
        max_pH = default_ph_range[1]
    else:
        min_pH = pH_range[0]
        max_pH = pH_range[1]

    pH_list = np.linspace(min_pH, max_pH, 1000)
    aH_list = list(map(pH2aH, pH_list))

    # get equilibrium constants
    logK_path = r"./data/log_K.csv"
    logK_df = pd.read_csv(logK_path, sep=',', index_col=0)

    k = {}
    k_keys = ['HS', 'H2S', 'HSO4', 'SO4', 'KSO4', 'NaSO4', 'CaSO4']
    k_values = logK_df.loc[T_c, k_keys]
    for i, k_key in enumerate(k_keys):
        k[k_key] = 10 ** (k_values.iloc[i])

    # get delta values
    delta_path = r"./data/delta_new.csv"
    delta_df = pd.read_csv(delta_path, sep=',', index_col=0)

    delta = {
        'totalS': delta_totalS
        }
    delta_keys = ['HS', 'S', 'HSO4', 'SO4', 'KSO4', 'NaSO4', 'CaSO4', 'FeS', 'ZnS', 'FeS2', 'PbS']
    delta_values = delta_df.loc[T_c, delta_keys]
    for i, delta_key in enumerate(delta_keys):
        delta[delta_key] = delta_values.iloc[i]

    # get activity coefficients
    T_and_I = f"{T_c}_{ionic_strength}"
    gamma_path = r"./data/gamma_new.csv"
    gamma_df = pd.read_csv(gamma_path, sep=',', index_col=0)

    gamma = {}
    gamma_keys = ['HS', 'H2S', 'HSO4', 'SO4', 'KSO4', 'NaSO4', 'CaSO4', 'Ca', 'K', 'Na', 'S']
    gamma_values = gamma_df.loc[T_and_I, gamma_keys]
    for i, gamma_key in enumerate(gamma_keys):
        gamma[gamma_key] = 10 ** (gamma_values.iloc[i])

    # plot
    plt.figure(figsize=figsize)
    # show both the image and contours
    img = plt.imread(f"imgs/{T_c}.png")
    plt.imshow(img, extent=[default_ph_range[0], default_ph_range[1], log_fo2_range[0], log_fo2_range[1]], aspect='auto')
    # plt.show()

    delta34S_H2S_list = []
    if plot_species == "H2S":
            delta34S_H2S_list = delta_list
    elif plot_species in delta_keys:
        delta34S_H2S_list = list(map(lambda x: x - delta[plot_species], delta_list))
    else:
        print("not supported species")

    del_num = 0
    for delta34S_H2S in delta34S_H2S_list:
        if delta34S_H2S - delta_totalS <= 0:
            logfO2_list, valid_pH_list, _ = calc_fO2(aH_list, delta34S_H2S, k, gamma, delta,params)
            print(min(logfO2_list), max(logfO2_list))
            plt.plot(valid_pH_list, logfO2_list)
        else:
            # delta34S_H2S > 0
            logfO2_list, valid_pH_list, invalid_valid_pH = calc_fO2(aH_list, delta34S_H2S, k, gamma, delta, params)
            logfO2_list, valid_pH_list, invalid_valid_pH, has_solution = get_valid_pH_list(invalid_valid_pH, max_pH, delta34S_H2S, k, gamma, delta, params)
            if not has_solution:
                del_index = delta34S_H2S_list.index(delta34S_H2S)
                del_value = delta_list.pop(del_index - del_num)
                del_num += 1
                print(f"plot_species: {del_value} is impossible in this system!")
            else:
                for _ in range(3):
                    logfO2_list, valid_pH_list, invalid_valid_pH, _ = get_valid_pH_list(invalid_valid_pH, max_pH, delta34S_H2S, k, gamma, delta, params)

                print(min(logfO2_list), max(logfO2_list))
                plt.plot(valid_pH_list, logfO2_list)

    plt.legend(delta_list)
    totalS = delta["totalS"]
    x_min, x_max = default_ph_range
    y_min, y_max = log_fo2_range
    mark_x = (x_min + x_max * 3) / 4
    mark_y = (y_min * 3 + y_max) / 4
    plt.text(mark_x, mark_y, f"{T_c}°C  δ34ΣS={totalS}", fontdict={"fontsize":9})
    xticks = np.linspace(default_ph_range[0], default_ph_range[1], default_ph_range[1] - default_ph_range[0] + 1)
    yticks = np.linspace(log_fo2_range[0], log_fo2_range[1], int(log_fo2_range[1] - log_fo2_range[0] + 1))
    plt.xticks(xticks)
    plt.yticks(yticks)

    
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # plt.xticks([])
    # plt.yticks([])
    plt.savefig(f"./output/{plot_species}_{T_c}C.pdf", dpi=300)
    plt.show()


if __name__=="__main__":
    T_c = 350
    delta_totalS = 5.0
    plot_species = "FeS2"
    delta_list = [-5, 1.8, 2.9, 3.6, 3.9, 6.0]
    ranges = {
        "pH": {
                350: (5.085, 6.400),
                300: (5.113, 6.517),
                250: (5.751, 6.621),
                0: (2, 12)
        },
            "log_fo2" : {
                350: (-36, -18),
                300: (-40, -22),
                250: (-46, -28)
            }
        }
    # default_ph_range为True时，将会取0~12的ph范围，适合用来画图；该值为False时，ph范围会随着ranges里的ph改变，适合用来计算精确log_fO2值。
    default_ph_range = (2, 12)
    use_default_ph_range = True
    print(f"{T_c} degree")
    main(T_c, delta_totalS, plot_species, delta_list, ranges["log_fo2"][T_c], ranges["pH"][T_c], default_ph_range=default_ph_range, use_default_ph_range=use_default_ph_range)
