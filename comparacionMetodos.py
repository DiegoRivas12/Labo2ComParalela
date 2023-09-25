import pylab as pl
import numpy as np
x = np.array([50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,1000,1010,1020,1030,1040])
primerMetodoClasico = np.array([0.001,0.001,0.001,0.001,0.002,0.002,0.004,0.004,0.006,0.007,0.008,0.01,0.011,0.014,0.016,0.018,0.021,0.024,0.029,0.032,0.036,0.04,0.044,0.056,0.063,0.067,0.069,0.081,0.087,0.098,0.108,0.118,0.122,0.142,0.157,0.177,0.191,0.213,0.23,0.258,0.271,0.288,0.324,0.333,0.355,0.386,0.411,0.438,0.455,0.485,0.522,0.536,0.567,0.593,0.63,0.662,0.779,0.815,0.819,0.842,1.474,1.282,1.465,1.71,2.387,2.743,2.83,1.937,1.439,1.423,1.359,1.508,1.571,1.52,2.568,2.218,1.942,2.205,2.096,2.419,2.642,2.427,2.396,2.591,2.465,2.597,2.576,2.918,4.551,4.428,3.79,3.62,3.801,3.403,3.984,4.675,4.929,6.479,5.193,4.948])
segundoMetodoBloques = np.array([0,0.001,0.001,0.001,0.002,0.002,0.003,0.004,0.006,0.008,0.008,0.009,0.012,0.013,0.016,0.017,0.02,0.025,0.026,0.03,0.033,0.039,0.046,0.049,0.057,0.063,0.068,0.075,0.078,0.112,0.098,0.111,0.113,0.126,0.137,0.148,0.168,0.19,0.208,0.231,0.242,0.259,0.299,0.293,0.313,0.344,0.353,0.373,0.46,0.507,0.482,0.509,0.513,0.51,0.548,0.748,0.603,0.659,0.687,0.701,0.725,0.764,0.818,0.913,1.008,0.937,0.998,1.097,1.063,1.1,1.153,1.389,1.359,1.819,1.733,1.454,1.565,1.534,1.851,2.796,2.583,2.063,1.979,2.056,2.322,2.108,2.196,3.576,2.862,2.976,2.98,3.782,3.342,3.334,4.227,3.883,4.114,3.987,3.284,3.435])
pl.plot(x,primerMetodoClasico, linewidth=1.0, linestyle="-",label="primerMetodoClasico")
pl.plot(x,segundoMetodoBloques, linewidth=1.0, linestyle="-",label="segundoMetodoBloques")
pl.legend(loc='upper left')
pl.title('repeticiones=100 incremento=10')

pl.show()