
class TiltCalc:
    #Data
    playerInstanceDataList = []

    #Tiltscore factors
    avg_deaths = 0
    avg_kills = 0
    avg_KD = 0
    losses = 0
    avg_cs = 0
    avg_int = 0

    #Tiltscore
    tiltscore = 0
    def __init__(self, playerInstanceDataList):
        self.playerInstanceDataList = playerInstanceDataList
        self.init_data()

    def init_data(self):  
        for i in range(len(self.playerInstanceDataList)):
            self.avg_deaths += self.playerInstanceDataList[i].deaths
        self.avg_deaths /= len(self.playerInstanceDataList)

        for i in range(len(self.playerInstanceDataList)):
            self.avg_kills += self.playerInstanceDataList[i].kills
        self.avg_kills /= len(self.playerInstanceDataList)

        self.avg_KD = self.avg_kills / self.avg_deaths

        for i in range(len(self.playerInstanceDataList)):
            self.avg_cs += self.playerInstanceDataList[i].cs
        self.avg_cs /= len(self.playerInstanceDataList)

        for i in range(len(self.playerInstanceDataList)):
            if self.playerInstanceDataList[i].possibly_inted == True:
                self.avg_int += 1
        self.avg_int /= len(self.playerInstanceDataList)


        # TODO - Not sure if losses is actually working
        for i in range(len(self.playerInstanceDataList)):
            if self.playerInstanceDataList[i].lost == True:
                self.losses += 1
        
        
    
        #self.tilt_calculation()
   #TODO def tilt_calculation(self):
