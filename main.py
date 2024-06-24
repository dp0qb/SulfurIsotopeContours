import CalcDeltaS as cds

T_c = 350
delta_totalS = 0
plot_species = "FeS2"

delta_list = [1.8, 6.9] # 350

ranges = {
    "pH": {
            350: (5.085, 6.400),
            300: (5.113, 6.517),
            250: (5.128, 6.621),
            0: (2, 12)
    },
    "log_fo2" : {
        350: (-36, -18),
        300: (-40, -22),
        250: (-46, -28)
    }
}
# default_ph_range的取值范围和底图一致即可
default_ph_range = (2, 12)
# use_default_ph_range为True时，将会取default_ph_range的ph范围，适合用来画图；该值为False时，ph范围会随着ranges里的ph改变，适合用来计算精确log_fO2值。
use_default_ph_range = False
print(f"{T_c} degree")
cds.main(T_c, delta_totalS, plot_species, delta_list, ranges["log_fo2"][T_c], ranges["pH"][T_c], default_ph_range=default_ph_range, use_default_ph_range=use_default_ph_range)