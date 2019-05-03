import pandas as pd

class AnomaliaNyomozo:
    def __init__(self,filename):
        """
        Initialization of AnomaliaNyomozo
        param: filename - Secrete file about anomaly information
        """
        if "secret" not in filename:
            print("Warning! The loaded filename does not contain world 'secret'!")
        self.df = pd.read_csv(filename)
        if len(self.df.columns)!=2:
            raise NotImplementedError("The columns number of loaded file is not 2!")
    def investigation(self,caseid):
        """
        Evaluate results of the anomaly detection methods
        param: caseid - simple id or list / series of ids
        """
        if type(caseid)==int:
            hit = self.df[ self.df['ID']==caseid ]
            if len(hit)!=1:
                raise NotImplementedError("Unknown id - "+str(caseid))
            return hit.iloc[0,1]
        else:
            caselist = list(caseid)
            self.df['tmp']=self.df['ID'].apply(lambda x: 1 if x in caselist else 0)
            ans = self.df[  self.df['tmp']==1 ].copy()
            ans = ans[['ID','titok']]
            print(ans['titok'].value_counts())
            if len(ans)!=len(caselist):
                print("Warning! The imput contains {} unknown id(s).".format(len(caselist)-len(ans)))
            return ans
            