import dict_funcs2 as orthograph
import fst_make as fst

fst.make_of_I2()
rulesbook = orthograph.errors_find("train_co.txt","train_wr.txt",2)
fst.Epsilon(rulesbook)

(cost_del,cost_sub,cost_swap,cost_ins) = orthograph.errors_find("train_co.txt","train_wr.txt",1)
fst.make_of_E(cost_swap,cost_del,cost_ins,cost_sub)
