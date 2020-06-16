import pandas as pd
column_names=["supplyAirTemp","supplyAirTempSp","outAirTemp","mixAirTemp","returnAirTemp","supplyFanStat","returnFanStat","supplyFanSpeed","returnFanSpeed","exDamp","outDamp","retDamp","coolingValve","heatingValve","staticPresSp","staticPres","ocModeInd","faultGT"]

healthy_1 = pd.date_range(start='2008-08-27', freq='T',periods=6*24*60) #end="2008-09-01",
healthy_2 = pd.date_range(start='2008-09-04', freq='T',periods=2*24*60 )#end="2008-09-05",
healthy_3 = pd.date_range(start="2009-02-11", freq="T",periods=24*60)
healthy_4 = pd.date_range(start="2009-05-06", freq="T",periods=3*24*60)#end="2009-05-08",
healthy_5 = pd.date_range(start="2009-05-15",freq="T",periods=24*60)

wrong_1_1 = pd.date_range(start="2008-02-12", freq="T",periods=24*60)
wrong_1_2 = pd.date_range(start="2008-05-07", freq="T",periods=24*60)
wrong_1_3 = pd.date_range(start="2008-05-08", freq="T",periods=24*60)
wrong_1_4 = pd.date_range(start="2007-09-05", freq="T",periods=24*60)
wrong_1_5 = pd.date_range(start="2007-09-06", freq="T",periods=24*60)

wrong_2 = pd.date_range(start="2007-08-28", freq="T", periods=3*24*60) #end="2007-08-30",

wrong_3_1 = pd.date_range(start="2008-05-06", freq="T",periods=24*60)
wrong_3_2 = pd.date_range(start="2007-08-31",freq="T",periods=24*60)
wrong_3_3 = pd.date_range(start="2008-05-15",freq="T",periods=24*60)

wrong_3_4 = pd.date_range(start="2007-09-01",freq="T",periods=2*24*60) # end="2007-09-02",

healthy = healthy_1.union_many([healthy_2, healthy_3, healthy_4, healthy_5])
wrong_1 = wrong_1_1.union_many([wrong_1_2, wrong_1_3, wrong_1_4, wrong_1_5])
wrong_3 = wrong_3_1.union_many([wrong_3_2, wrong_3_3,wrong_3_4])
unhealthy = wrong_1.union_many([wrong_2,wrong_3])

healthy_exp_1=pd.date_range(start='2008-08-19', freq='T',periods=24*60)
healthy_exp_2=pd.date_range(start='2008-08-25', freq='T',periods=24*60)
healthy_exp_3=pd.date_range(start='2008-09-04', freq='T',periods=24*60)
healthy_exp_4=pd.date_range(start='2009-01-19', freq='T',periods=24*60)
healthy_exp_5=pd.date_range(start='2009-02-16', freq='T',periods=2*24*60)
healthy_exp_6=pd.date_range(start='2009-05-03', freq='T',periods=4*24*60)
healthy_exp_7=pd.date_range(start='2009-05-30', freq='T',periods=2*24*60)

healthy_exp = healthy_exp_1.union_many([healthy_exp_2, healthy_exp_3, healthy_exp_4, healthy_exp_5, healthy_exp_6,healthy_exp_7])
wrong_exp =  pd.date_range(start="2007-08-28", freq="T", periods=3*24*60)


