# -*- coding: utf-8 -*-
"""
Highstock Demos
Flags marking events: http://www.highcharts.com/stock/demo/flags-general
"""

import datetime
from highcharts import Highstock
H = Highstock()

data = [
[datetime.datetime(2013,6,2),0.7695],
[datetime.datetime(2013,6,3),0.7648],
[datetime.datetime(2013,6,4),0.7645],
[datetime.datetime(2013,6,5),0.7638],
[datetime.datetime(2013,6,6),0.7549],
[datetime.datetime(2013,6,7),0.7562],
[datetime.datetime(2013,6,9),0.7574],
[datetime.datetime(2013,6,10),0.7543],
[datetime.datetime(2013,6,11),0.7510],
[datetime.datetime(2013,6,12),0.7498],
[datetime.datetime(2013,6,13),0.7477],
[datetime.datetime(2013,6,14),0.7492],
[datetime.datetime(2013,6,16),0.7487],
[datetime.datetime(2013,6,17),0.7480],
[datetime.datetime(2013,6,18),0.7466],
[datetime.datetime(2013,6,19),0.7521],
[datetime.datetime(2013,6,20),0.7564],
[datetime.datetime(2013,6,21),0.7621],
[datetime.datetime(2013,6,23),0.7630],
[datetime.datetime(2013,6,24),0.7623],
[datetime.datetime(2013,6,25),0.7644],
[datetime.datetime(2013,6,26),0.7685],
[datetime.datetime(2013,6,27),0.7671],
[datetime.datetime(2013,6,28),0.7687],
[datetime.datetime(2013,6,30),0.7687],
[datetime.datetime(2013,7,1),0.7654],
[datetime.datetime(2013,7,2),0.7705],
[datetime.datetime(2013,7,3),0.7687],
[datetime.datetime(2013,7,4),0.7744],
[datetime.datetime(2013,7,5),0.7793],
[datetime.datetime(2013,7,7),0.7804],
[datetime.datetime(2013,7,8),0.7770],
[datetime.datetime(2013,7,9),0.7824],
[datetime.datetime(2013,7,10),0.7705],
[datetime.datetime(2013,7,11),0.7635],
[datetime.datetime(2013,7,12),0.7652],
[datetime.datetime(2013,7,14),0.7656],
[datetime.datetime(2013,7,15),0.7655],
[datetime.datetime(2013,7,16),0.7598],
[datetime.datetime(2013,7,17),0.7619],
[datetime.datetime(2013,7,18),0.7628],
[datetime.datetime(2013,7,19),0.7609],
[datetime.datetime(2013,7,21),0.7599],
[datetime.datetime(2013,7,22),0.7584],
[datetime.datetime(2013,7,23),0.7562],
[datetime.datetime(2013,7,24),0.7575],
[datetime.datetime(2013,7,25),0.7531],
[datetime.datetime(2013,7,26),0.7530],
[datetime.datetime(2013,7,28),0.7526],
[datetime.datetime(2013,7,29),0.7540],
[datetime.datetime(2013,7,30),0.7540],
[datetime.datetime(2013,7,31),0.7518],
[datetime.datetime(2013,8,1),0.7571],
[datetime.datetime(2013,8,2),0.7529],
[datetime.datetime(2013,8,4),0.7532],
[datetime.datetime(2013,8,5),0.7542],
[datetime.datetime(2013,8,6),0.7515],
[datetime.datetime(2013,8,7),0.7498],
[datetime.datetime(2013,8,8),0.7473],
[datetime.datetime(2013,8,9),0.7494],
[datetime.datetime(2013,8,11),0.7497],
[datetime.datetime(2013,8,12),0.7519],
[datetime.datetime(2013,8,13),0.7540],
[datetime.datetime(2013,8,14),0.7543],
[datetime.datetime(2013,8,15),0.7492],
[datetime.datetime(2013,8,16),0.7502],
[datetime.datetime(2013,8,18),0.7503],
[datetime.datetime(2013,8,19),0.7499],
[datetime.datetime(2013,8,20),0.7453],
[datetime.datetime(2013,8,21),0.7487],
[datetime.datetime(2013,8,22),0.7487],
[datetime.datetime(2013,8,23),0.7472],
[datetime.datetime(2013,8,25),0.7471],
[datetime.datetime(2013,8,26),0.7480],
[datetime.datetime(2013,8,27),0.7467],
[datetime.datetime(2013,8,28),0.7497],
[datetime.datetime(2013,8,29),0.7552],
[datetime.datetime(2013,8,30),0.7562],
[datetime.datetime(2013,9,1),0.7572],
[datetime.datetime(2013,9,2),0.7581],
[datetime.datetime(2013,9,3),0.7593],
[datetime.datetime(2013,9,4),0.7571],
[datetime.datetime(2013,9,5),0.7622],
[datetime.datetime(2013,9,6),0.7588],
[datetime.datetime(2013,9,8),0.7591],
[datetime.datetime(2013,9,9),0.7544],
[datetime.datetime(2013,9,10),0.7537],
[datetime.datetime(2013,9,11),0.7512],
[datetime.datetime(2013,9,12),0.7519],
[datetime.datetime(2013,9,13),0.7522],
[datetime.datetime(2013,9,15),0.7486],
[datetime.datetime(2013,9,16),0.7500],
[datetime.datetime(2013,9,17),0.7486],
[datetime.datetime(2013,9,18),0.7396],
[datetime.datetime(2013,9,19),0.7391],
[datetime.datetime(2013,9,20),0.7394],
[datetime.datetime(2013,9,22),0.7389],
[datetime.datetime(2013,9,23),0.7411],
[datetime.datetime(2013,9,24),0.7422],
[datetime.datetime(2013,9,25),0.7393],
[datetime.datetime(2013,9,26),0.7413],
[datetime.datetime(2013,9,27),0.7396],
[datetime.datetime(2013,9,29),0.7410],
[datetime.datetime(2013,9,30),0.7393],
[datetime.datetime(2013,10,1),0.7393],
[datetime.datetime(2013,10,2),0.7365],
[datetime.datetime(2013,10,3),0.7343],
[datetime.datetime(2013,10,4),0.7376],
[datetime.datetime(2013,10,6),0.7370],
[datetime.datetime(2013,10,7),0.7362],
[datetime.datetime(2013,10,8),0.7368],
[datetime.datetime(2013,10,9),0.7393],
[datetime.datetime(2013,10,10),0.7397],
[datetime.datetime(2013,10,11),0.7385],
[datetime.datetime(2013,10,13),0.7377],
[datetime.datetime(2013,10,14),0.7374],
[datetime.datetime(2013,10,15),0.7395],
[datetime.datetime(2013,10,16),0.7389],
[datetime.datetime(2013,10,17),0.7312],
[datetime.datetime(2013,10,18),0.7307],
[datetime.datetime(2013,10,20),0.7309],
[datetime.datetime(2013,10,21),0.7308],
[datetime.datetime(2013,10,22),0.7256],
[datetime.datetime(2013,10,23),0.7258],
[datetime.datetime(2013,10,24),0.7247],
[datetime.datetime(2013,10,25),0.7244],
[datetime.datetime(2013,10,27),0.7244],
[datetime.datetime(2013,10,28),0.7255],
[datetime.datetime(2013,10,29),0.7275],
[datetime.datetime(2013,10,30),0.7280],
[datetime.datetime(2013,10,31),0.7361],
[datetime.datetime(2013,11,1),0.7415],
[datetime.datetime(2013,11,3),0.7411],
[datetime.datetime(2013,11,4),0.7399],
[datetime.datetime(2013,11,5),0.7421],
[datetime.datetime(2013,11,6),0.7400],
[datetime.datetime(2013,11,7),0.7452],
[datetime.datetime(2013,11,8),0.7479],
[datetime.datetime(2013,11,10),0.7492],
[datetime.datetime(2013,11,11),0.7460],
[datetime.datetime(2013,11,12),0.7442],
[datetime.datetime(2013,11,13),0.7415],
[datetime.datetime(2013,11,14),0.7429],
[datetime.datetime(2013,11,15),0.7410],
[datetime.datetime(2013,11,17),0.7417],
[datetime.datetime(2013,11,18),0.7405],
[datetime.datetime(2013,11,19),0.7386],
[datetime.datetime(2013,11,20),0.7441],
[datetime.datetime(2013,11,21),0.7418],
[datetime.datetime(2013,11,22),0.7376],
[datetime.datetime(2013,11,24),0.7379],
[datetime.datetime(2013,11,25),0.7399],
[datetime.datetime(2013,11,26),0.7369],
[datetime.datetime(2013,11,27),0.7365],
[datetime.datetime(2013,11,28),0.7350],
[datetime.datetime(2013,11,29),0.7358],
[datetime.datetime(2013,12,1),0.7362],
[datetime.datetime(2013,12,2),0.7385],
[datetime.datetime(2013,12,3),0.7359],
[datetime.datetime(2013,12,4),0.7357],
[datetime.datetime(2013,12,5),0.7317],
[datetime.datetime(2013,12,6),0.7297],
[datetime.datetime(2013,12,8),0.7296],
[datetime.datetime(2013,12,9),0.7279],
[datetime.datetime(2013,12,10),0.7267],
[datetime.datetime(2013,12,11),0.7254],
[datetime.datetime(2013,12,12),0.7270],
[datetime.datetime(2013,12,13),0.7276],
[datetime.datetime(2013,12,15),0.7278],
[datetime.datetime(2013,12,16),0.7267],
[datetime.datetime(2013,12,17),0.7263],
[datetime.datetime(2013,12,18),0.7307],
[datetime.datetime(2013,12,19),0.7319],
[datetime.datetime(2013,12,20),0.7315],
[datetime.datetime(2013,12,22),0.7311],
[datetime.datetime(2013,12,23),0.7301],
[datetime.datetime(2013,12,24),0.7308],
[datetime.datetime(2013,12,25),0.7310],
[datetime.datetime(2013,12,26),0.7304],
[datetime.datetime(2013,12,27),0.7277],
[datetime.datetime(2013,12,29),0.7272],
[datetime.datetime(2013,12,30),0.7244],
[datetime.datetime(2013,12,31),0.7275],
[datetime.datetime(2014,1,1),0.7271],
[datetime.datetime(2014,1,2),0.7314],
[datetime.datetime(2014,1,3),0.7359],
[datetime.datetime(2014,1,5),0.7355],
[datetime.datetime(2014,1,6),0.7338],
[datetime.datetime(2014,1,7),0.7345],
[datetime.datetime(2014,1,8),0.7366],
[datetime.datetime(2014,1,9),0.7349],
[datetime.datetime(2014,1,10),0.7316],
[datetime.datetime(2014,1,12),0.7315],
[datetime.datetime(2014,1,13),0.7315],
[datetime.datetime(2014,1,14),0.7310],
[datetime.datetime(2014,1,15),0.7350],
[datetime.datetime(2014,1,16),0.7341],
[datetime.datetime(2014,1,17),0.7385],
[datetime.datetime(2014,1,19),0.7392],
[datetime.datetime(2014,1,20),0.7379],
[datetime.datetime(2014,1,21),0.7373],
[datetime.datetime(2014,1,22),0.7381],
[datetime.datetime(2014,1,23),0.7301],
[datetime.datetime(2014,1,24),0.7311],
[datetime.datetime(2014,1,26),0.7306],
[datetime.datetime(2014,1,27),0.7314],
[datetime.datetime(2014,1,28),0.7316],
[datetime.datetime(2014,1,29),0.7319],
[datetime.datetime(2014,1,30),0.7377],
[datetime.datetime(2014,1,31),0.7415],
[datetime.datetime(2014,2,2),0.7414],
[datetime.datetime(2014,2,3),0.7393],
[datetime.datetime(2014,2,4),0.7397],
[datetime.datetime(2014,2,5),0.7389],
[datetime.datetime(2014,2,6),0.7358],
[datetime.datetime(2014,2,7),0.7334],
[datetime.datetime(2014,2,9),0.7343],
[datetime.datetime(2014,2,10),0.7328],
[datetime.datetime(2014,2,11),0.7332],
[datetime.datetime(2014,2,12),0.7356],
[datetime.datetime(2014,2,13),0.7309],
[datetime.datetime(2014,2,14),0.7304],
[datetime.datetime(2014,2,16),0.7300],
[datetime.datetime(2014,2,17),0.7295],
[datetime.datetime(2014,2,18),0.7268],
[datetime.datetime(2014,2,19),0.7281],
[datetime.datetime(2014,2,20),0.7289],
[datetime.datetime(2014,2,21),0.7278],
[datetime.datetime(2014,2,23),0.7280],
[datetime.datetime(2014,2,24),0.7280],
[datetime.datetime(2014,2,25),0.7275],
[datetime.datetime(2014,2,26),0.7306],
[datetime.datetime(2014,2,27),0.7295],
[datetime.datetime(2014,2,28),0.7245],
[datetime.datetime(2014,3,2),0.7259],
[datetime.datetime(2014,3,3),0.7280],
[datetime.datetime(2014,3,4),0.7276],
[datetime.datetime(2014,3,5),0.7282],
[datetime.datetime(2014,3,6),0.7215],
[datetime.datetime(2014,3,7),0.7206],
[datetime.datetime(2014,3,9),0.7206],
[datetime.datetime(2014,3,10),0.7207],
[datetime.datetime(2014,3,11),0.7216],
[datetime.datetime(2014,3,12),0.7192],
[datetime.datetime(2014,3,13),0.7210],
[datetime.datetime(2014,3,14),0.7187],
[datetime.datetime(2014,3,16),0.7188],
[datetime.datetime(2014,3,17),0.7183],
[datetime.datetime(2014,3,18),0.7177],
[datetime.datetime(2014,3,19),0.7229],
[datetime.datetime(2014,3,20),0.7258],
[datetime.datetime(2014,3,21),0.7249],
[datetime.datetime(2014,3,23),0.7247],
[datetime.datetime(2014,3,24),0.7226],
[datetime.datetime(2014,3,25),0.7232],
[datetime.datetime(2014,3,26),0.7255],
[datetime.datetime(2014,3,27),0.7278],
[datetime.datetime(2014,3,28),0.7271],
[datetime.datetime(2014,3,30),0.7272],
[datetime.datetime(2014,3,31),0.7261],
[datetime.datetime(2014,4,1),0.7250],
[datetime.datetime(2014,4,2),0.7264],
[datetime.datetime(2014,4,3),0.7289],
[datetime.datetime(2014,4,4),0.7298],
[datetime.datetime(2014,4,6),0.7298],
[datetime.datetime(2014,4,7),0.7278],
[datetime.datetime(2014,4,8),0.7248],
[datetime.datetime(2014,4,9),0.7218],
[datetime.datetime(2014,4,10),0.7200],
[datetime.datetime(2014,4,11),0.7202],
[datetime.datetime(2014,4,13),0.7222],
[datetime.datetime(2014,4,14),0.7236],
[datetime.datetime(2014,4,15),0.7239],
[datetime.datetime(2014,4,16),0.7238],
[datetime.datetime(2014,4,17),0.7238],
[datetime.datetime(2014,4,18),0.7238],
[datetime.datetime(2014,4,20),0.7239],
[datetime.datetime(2014,4,21),0.7250],
[datetime.datetime(2014,4,22),0.7244],
[datetime.datetime(2014,4,23),0.7238],
[datetime.datetime(2014,4,24),0.7229],
[datetime.datetime(2014,4,25),0.7229],
[datetime.datetime(2014,4,27),0.7226],
[datetime.datetime(2014,4,28),0.7220],
[datetime.datetime(2014,4,29),0.7240],
[datetime.datetime(2014,4,30),0.7211],
[datetime.datetime(2014,5,1),0.7210],
[datetime.datetime(2014,5,2),0.7209],
[datetime.datetime(2014,5,4),0.7209],
[datetime.datetime(2014,5,5),0.7207],
[datetime.datetime(2014,5,6),0.7180],
[datetime.datetime(2014,5,7),0.7188],
[datetime.datetime(2014,5,8),0.7225],
[datetime.datetime(2014,5,9),0.7268],
[datetime.datetime(2014,5,11),0.7267],
[datetime.datetime(2014,5,12),0.7269],
[datetime.datetime(2014,5,13),0.7297],
[datetime.datetime(2014,5,14),0.7291],
[datetime.datetime(2014,5,15),0.7294],
[datetime.datetime(2014,5,16),0.7302],
[datetime.datetime(2014,5,18),0.7298],
[datetime.datetime(2014,5,19),0.7295],
[datetime.datetime(2014,5,20),0.7298],
[datetime.datetime(2014,5,21),0.7307],
[datetime.datetime(2014,5,22),0.7323],
[datetime.datetime(2014,5,23),0.7335],
[datetime.datetime(2014,5,25),0.7338],
[datetime.datetime(2014,5,26),0.7329],
[datetime.datetime(2014,5,27),0.7335],
[datetime.datetime(2014,5,28),0.7358],
[datetime.datetime(2014,5,29),0.7351],
[datetime.datetime(2014,5,30),0.7337],
[datetime.datetime(2014,6,1),0.7338],
[datetime.datetime(2014,6,2),0.7355],
[datetime.datetime(2014,6,3),0.7338],
[datetime.datetime(2014,6,4),0.7353],
[datetime.datetime(2014,6,5),0.7321],
[datetime.datetime(2014,6,6),0.7330],
[datetime.datetime(2014,6,8),0.7327],
[datetime.datetime(2014,6,9),0.7356],
[datetime.datetime(2014,6,10),0.7381],
[datetime.datetime(2014,6,11),0.7389],
[datetime.datetime(2014,6,12),0.7379],
[datetime.datetime(2014,6,13),0.7384],
[datetime.datetime(2014,6,15),0.7388],
[datetime.datetime(2014,6,16),0.7367],
[datetime.datetime(2014,6,17),0.7382],
[datetime.datetime(2014,6,18),0.7356],
[datetime.datetime(2014,6,19),0.7349],
[datetime.datetime(2014,6,20),0.7353],
[datetime.datetime(2014,6,22),0.7357],
[datetime.datetime(2014,6,23),0.7350],
[datetime.datetime(2014,6,24),0.7350],
[datetime.datetime(2014,6,25),0.7337],
[datetime.datetime(2014,6,26),0.7347],
[datetime.datetime(2014,6,27),0.7327],
[datetime.datetime(2014,6,29),0.7330],
[datetime.datetime(2014,6,30),0.7304],
[datetime.datetime(2014,7,1),0.7310],
[datetime.datetime(2014,7,2),0.7320],
[datetime.datetime(2014,7,3),0.7347],
[datetime.datetime(2014,7,4),0.7356],
[datetime.datetime(2014,7,6),0.7360],
[datetime.datetime(2014,7,7),0.7350],
[datetime.datetime(2014,7,8),0.7346],
[datetime.datetime(2014,7,9),0.7329],
[datetime.datetime(2014,7,10),0.7348],
[datetime.datetime(2014,7,11),0.7349],
[datetime.datetime(2014,7,13),0.7352],
[datetime.datetime(2014,7,14),0.7342],
[datetime.datetime(2014,7,15),0.7369],
[datetime.datetime(2014,7,16),0.7393],
[datetime.datetime(2014,7,17),0.7392],
[datetime.datetime(2014,7,18),0.7394],
[datetime.datetime(2014,7,20),0.7390],
[datetime.datetime(2014,7,21),0.7395],
[datetime.datetime(2014,7,22),0.7427],
[datetime.datetime(2014,7,23),0.7427],
[datetime.datetime(2014,7,24),0.7428],
[datetime.datetime(2014,7,25),0.7446],
[datetime.datetime(2014,7,27),0.7447],
[datetime.datetime(2014,7,28),0.7440],
[datetime.datetime(2014,7,29),0.7458],
[datetime.datetime(2014,7,30),0.7464],
[datetime.datetime(2014,7,31),0.7469],
[datetime.datetime(2014,8,1),0.7446],
[datetime.datetime(2014,8,3),0.7447],
[datetime.datetime(2014,8,4),0.7450],
[datetime.datetime(2014,8,5),0.7477],
[datetime.datetime(2014,8,6),0.7472],
[datetime.datetime(2014,8,7),0.7483],
[datetime.datetime(2014,8,8),0.7457],
[datetime.datetime(2014,8,10),0.7460],
[datetime.datetime(2014,8,11),0.7470],
[datetime.datetime(2014,8,12),0.7480],
[datetime.datetime(2014,8,13),0.7482],
[datetime.datetime(2014,8,14),0.7482],
[datetime.datetime(2014,8,15),0.7463],
[datetime.datetime(2014,8,17),0.7469],
[datetime.datetime(2014,8,18),0.7483],
[datetime.datetime(2014,8,19),0.7508],
[datetime.datetime(2014,8,20),0.7541],
[datetime.datetime(2014,8,21),0.7529],
[datetime.datetime(2014,8,22),0.7551],
[datetime.datetime(2014,8,24),0.7577],
[datetime.datetime(2014,8,25),0.7580],
[datetime.datetime(2014,8,26),0.7593],
[datetime.datetime(2014,8,27),0.7580],
[datetime.datetime(2014,8,28),0.7585],
[datetime.datetime(2014,8,29),0.7614],
[datetime.datetime(2014,8,31),0.7618],
[datetime.datetime(2014,9,1),0.7618],
[datetime.datetime(2014,9,2),0.7614],
[datetime.datetime(2014,9,3),0.7604],
[datetime.datetime(2014,9,4),0.7725],
[datetime.datetime(2014,9,5),0.7722],
[datetime.datetime(2014,9,7),0.7721],
[datetime.datetime(2014,9,8),0.7753],
[datetime.datetime(2014,9,9),0.7730],
[datetime.datetime(2014,9,10),0.7742],
[datetime.datetime(2014,9,11),0.7736],
[datetime.datetime(2014,9,12),0.7713],
[datetime.datetime(2014,9,14),0.7717],
[datetime.datetime(2014,9,15),0.7727],
[datetime.datetime(2014,9,16),0.7716],
[datetime.datetime(2014,9,17),0.7772],
[datetime.datetime(2014,9,18),0.7739],
[datetime.datetime(2014,9,19),0.7794],
[datetime.datetime(2014,9,21),0.7788],
[datetime.datetime(2014,9,22),0.7782],
[datetime.datetime(2014,9,23),0.7784],
[datetime.datetime(2014,9,24),0.7824],
[datetime.datetime(2014,9,25),0.7843],
[datetime.datetime(2014,9,26),0.7884],
[datetime.datetime(2014,9,28),0.7891],
[datetime.datetime(2014,9,29),0.7883],
[datetime.datetime(2014,9,30),0.7916],
[datetime.datetime(2014,10,1),0.7922],
[datetime.datetime(2014,10,2),0.7893],
[datetime.datetime(2014,10,3),0.7989],
[datetime.datetime(2014,10,5),0.7992],
[datetime.datetime(2014,10,6),0.7903],
[datetime.datetime(2014,10,7),0.7893],
[datetime.datetime(2014,10,8),0.7853],
[datetime.datetime(2014,10,9),0.7880],
[datetime.datetime(2014,10,10),0.7919],
[datetime.datetime(2014,10,12),0.7912],
[datetime.datetime(2014,10,13),0.7842],
[datetime.datetime(2014,10,14),0.7900],
[datetime.datetime(2014,10,15),0.7790],
[datetime.datetime(2014,10,16),0.7806],
[datetime.datetime(2014,10,17),0.7835],
[datetime.datetime(2014,10,19),0.7844],
[datetime.datetime(2014,10,20),0.7813],
[datetime.datetime(2014,10,21),0.7864],
[datetime.datetime(2014,10,22),0.7905],
[datetime.datetime(2014,10,23),0.7907],
[datetime.datetime(2014,10,24),0.7893],
[datetime.datetime(2014,10,26),0.7889],
[datetime.datetime(2014,10,27),0.7875],
[datetime.datetime(2014,10,28),0.7853],
[datetime.datetime(2014,10,29),0.7916],
[datetime.datetime(2014,10,30),0.7929],
[datetime.datetime(2014,10,31),0.7984],
[datetime.datetime(2014,11,2),0.7999],
[datetime.datetime(2014,11,3),0.8012],
[datetime.datetime(2014,11,4),0.7971],
[datetime.datetime(2014,11,5),0.8009],
[datetime.datetime(2014,11,6),0.8081],
[datetime.datetime(2014,11,7),0.8030],
[datetime.datetime(2014,11,9),0.8025],
[datetime.datetime(2014,11,10),0.8051],
[datetime.datetime(2014,11,11),0.8016],
[datetime.datetime(2014,11,12),0.8040],
[datetime.datetime(2014,11,13),0.8015],
[datetime.datetime(2014,11,14),0.7985],
[datetime.datetime(2014,11,16),0.7988],
[datetime.datetime(2014,11,17),0.8032],
[datetime.datetime(2014,11,18),0.7976],
[datetime.datetime(2014,11,19),0.7965],
[datetime.datetime(2014,11,20),0.7975],
[datetime.datetime(2014,11,21),0.8071],
[datetime.datetime(2014,11,23),0.8082],
[datetime.datetime(2014,11,24),0.8037],
[datetime.datetime(2014,11,25),0.8016],
[datetime.datetime(2014,11,26),0.7996],
[datetime.datetime(2014,11,27),0.8022],
[datetime.datetime(2014,11,28),0.8031],
[datetime.datetime(2014,11,30),0.8040],
[datetime.datetime(2014,12,1),0.8020],
[datetime.datetime(2014,12,2),0.8075],
[datetime.datetime(2014,12,3),0.8123],
[datetime.datetime(2014,12,4),0.8078],
[datetime.datetime(2014,12,5),0.8139],
[datetime.datetime(2014,12,7),0.8135],
[datetime.datetime(2014,12,8),0.8119],
[datetime.datetime(2014,12,9),0.8081],
[datetime.datetime(2014,12,10),0.8034],
[datetime.datetime(2014,12,11),0.8057],
[datetime.datetime(2014,12,12),0.8024],
[datetime.datetime(2014,12,14),0.8024],
[datetime.datetime(2014,12,15),0.8040],
[datetime.datetime(2014,12,16),0.7993],
[datetime.datetime(2014,12,17),0.8102],
[datetime.datetime(2014,12,18),0.8139],
[datetime.datetime(2014,12,19),0.8177],
[datetime.datetime(2014,12,21),0.8180],
[datetime.datetime(2014,12,22),0.8176],
[datetime.datetime(2014,12,23),0.8215],
[datetime.datetime(2014,12,24),0.8200],
[datetime.datetime(2014,12,25),0.8182],
[datetime.datetime(2014,12,26),0.8213],
[datetime.datetime(2014,12,28),0.8218],
[datetime.datetime(2014,12,29),0.8229],
[datetime.datetime(2014,12,30),0.8225],
[datetime.datetime(2014,12,31),0.8266],
[datetime.datetime(2015,1,1),0.8262],
[datetime.datetime(2015,1,2),0.8331],
[datetime.datetime(2015,1,4),0.8371],
[datetime.datetime(2015,1,5),0.8380],
[datetime.datetime(2015,1,6),0.8411],
[datetime.datetime(2015,1,7),0.8447],
[datetime.datetime(2015,1,8),0.8480],
[datetime.datetime(2015,1,9),0.8445],
[datetime.datetime(2015,1,11),0.8425],
[datetime.datetime(2015,1,12),0.8451],
[datetime.datetime(2015,1,13),0.8495],
[datetime.datetime(2015,1,14),0.8482],
[datetime.datetime(2015,1,15),0.8598],
[datetime.datetime(2015,1,16),0.8643],
[datetime.datetime(2015,1,18),0.8648],
[datetime.datetime(2015,1,19),0.8617],
[datetime.datetime(2015,1,20),0.8658],
[datetime.datetime(2015,1,21),0.8613],
[datetime.datetime(2015,1,22),0.8798],
[datetime.datetime(2015,1,23),0.8922],
[datetime.datetime(2015,1,25),0.8990],
[datetime.datetime(2015,1,26),0.8898],
[datetime.datetime(2015,1,27),0.8787],
[datetime.datetime(2015,1,28),0.8859],
[datetime.datetime(2015,1,29),0.8834],
[datetime.datetime(2015,1,30),0.8859],
[datetime.datetime(2015,2,1),0.8843],
[datetime.datetime(2015,2,2),0.8817],
[datetime.datetime(2015,2,3),0.8710],
[datetime.datetime(2015,2,4),0.8813],
[datetime.datetime(2015,2,5),0.8713],
[datetime.datetime(2015,2,6),0.8837],
[datetime.datetime(2015,2,8),0.8839],
[datetime.datetime(2015,2,9),0.8831],
[datetime.datetime(2015,2,10),0.8833],
[datetime.datetime(2015,2,11),0.8823],
[datetime.datetime(2015,2,12),0.8770],
[datetime.datetime(2015,2,13),0.8783],
[datetime.datetime(2015,2,15),0.8774],
[datetime.datetime(2015,2,16),0.8807],
[datetime.datetime(2015,2,17),0.8762],
[datetime.datetime(2015,2,18),0.8774],
[datetime.datetime(2015,2,19),0.8798],
[datetime.datetime(2015,2,20),0.8787],
[datetime.datetime(2015,2,22),0.8787],
[datetime.datetime(2015,2,23),0.8824],
[datetime.datetime(2015,2,24),0.8818],
[datetime.datetime(2015,2,25),0.8801],
[datetime.datetime(2015,2,26),0.8931],
[datetime.datetime(2015,2,27),0.8932],
[datetime.datetime(2015,3,1),0.8960],
[datetime.datetime(2015,3,2),0.8941],
[datetime.datetime(2015,3,3),0.8948],
[datetime.datetime(2015,3,4),0.9026],
[datetime.datetime(2015,3,5),0.9066],
[datetime.datetime(2015,3,6),0.9222],
[datetime.datetime(2015,3,8),0.9221],
[datetime.datetime(2015,3,9),0.9214],
[datetime.datetime(2015,3,10),0.9347],
[datetime.datetime(2015,3,11),0.9482],
[datetime.datetime(2015,3,12),0.9403],
[datetime.datetime(2015,3,13),0.9528],
[datetime.datetime(2015,3,15),0.9541],
[datetime.datetime(2015,3,16),0.9462],
[datetime.datetime(2015,3,17),0.9435],
[datetime.datetime(2015,3,18),0.9203],
[datetime.datetime(2015,3,19),0.9381],
[datetime.datetime(2015,3,20),0.9241],
[datetime.datetime(2015,3,22),0.9237],
[datetime.datetime(2015,3,23),0.9135],
[datetime.datetime(2015,3,24),0.9152],
[datetime.datetime(2015,3,25),0.9114],
[datetime.datetime(2015,3,26),0.9188],
[datetime.datetime(2015,3,27),0.9184],
[datetime.datetime(2015,3,29),0.9188],
[datetime.datetime(2015,3,30),0.9231],
[datetime.datetime(2015,3,31),0.9319],
[datetime.datetime(2015,4,1),0.9291],
[datetime.datetime(2015,4,2),0.9188],
[datetime.datetime(2015,4,3),0.9109],
[datetime.datetime(2015,4,5),0.9091],
[datetime.datetime(2015,4,6),0.9154],
[datetime.datetime(2015,4,7),0.9246],
[datetime.datetime(2015,4,8),0.9276],
[datetime.datetime(2015,4,9),0.9382],
[datetime.datetime(2015,4,10),0.9431],
[datetime.datetime(2015,4,12),0.9426],
[datetime.datetime(2015,4,13),0.9463],
[datetime.datetime(2015,4,14),0.9386],
[datetime.datetime(2015,4,15),0.9357],
[datetime.datetime(2015,4,16),0.9293],
[datetime.datetime(2015,4,17),0.9254],
[datetime.datetime(2015,4,19),0.9251],
[datetime.datetime(2015,4,20),0.9312],
[datetime.datetime(2015,4,21),0.9315],
[datetime.datetime(2015,4,22),0.9323],
[datetime.datetime(2015,4,23),0.9236],
[datetime.datetime(2015,4,24),0.9196],
[datetime.datetime(2015,4,26),0.9201],
[datetime.datetime(2015,4,27),0.9184],
[datetime.datetime(2015,4,28),0.9106],
[datetime.datetime(2015,4,29),0.8983],
[datetime.datetime(2015,4,30),0.8909],
[datetime.datetime(2015,5,1),0.8928],
[datetime.datetime(2015,5,3),0.8941],
[datetime.datetime(2015,5,4),0.8972],
[datetime.datetime(2015,5,5),0.8940],
[datetime.datetime(2015,5,6),0.8808],
[datetime.datetime(2015,5,7),0.8876],
[datetime.datetime(2015,5,8),0.8925],
[datetime.datetime(2015,5,10),0.8934],
[datetime.datetime(2015,5,11),0.8964],
[datetime.datetime(2015,5,12),0.8917],
[datetime.datetime(2015,5,13),0.8805],
[datetime.datetime(2015,5,14),0.8764],
[datetime.datetime(2015,5,15),0.8732],
[datetime.datetime(2015,5,17),0.8737],
[datetime.datetime(2015,5,18),0.8838],
[datetime.datetime(2015,5,19),0.8969],
[datetime.datetime(2015,5,20),0.9014],
[datetime.datetime(2015,5,21),0.8999],
[datetime.datetime(2015,5,22),0.9076],
[datetime.datetime(2015,5,24),0.9098],
[datetime.datetime(2015,5,25),0.9110],
[datetime.datetime(2015,5,26),0.9196],
[datetime.datetime(2015,5,27),0.9170],
[datetime.datetime(2015,5,28),0.9133],
[datetime.datetime(2015,5,29),0.9101],
[datetime.datetime(2015,5,31),0.9126],
[datetime.datetime(2015,6,1),0.9151],
[datetime.datetime(2015,6,2),0.8965],
[datetime.datetime(2015,6,3),0.8871],
[datetime.datetime(2015,6,4),0.8898],
[datetime.datetime(2015,6,5),0.8999],
[datetime.datetime(2015,6,7),0.9004],
[datetime.datetime(2015,6,8),0.8857],
[datetime.datetime(2015,6,9),0.8862],
[datetime.datetime(2015,6,10),0.8829],
[datetime.datetime(2015,6,11),0.8882],
[datetime.datetime(2015,6,12),0.8873],
[datetime.datetime(2015,6,14),0.8913],
[datetime.datetime(2015,6,15),0.8862],
[datetime.datetime(2015,6,16),0.8891],
[datetime.datetime(2015,6,17),0.8821],
[datetime.datetime(2015,6,18),0.8802],
[datetime.datetime(2015,6,19),0.8808],
[datetime.datetime(2015,6,21),0.8794],
[datetime.datetime(2015,6,22),0.8818],
[datetime.datetime(2015,6,23),0.8952],
[datetime.datetime(2015,6,24),0.8924],
[datetime.datetime(2015,6,25),0.8925],
[datetime.datetime(2015,6,26),0.8955],
[datetime.datetime(2015,6,28),0.9113],
[datetime.datetime(2015,6,29),0.8900],
[datetime.datetime(2015,6,30),0.8950]
]

data2 = [{
        'x' : datetime.datetime(2015, 6, 8),
        'title' : 'C',
        'text' : 'Stocks fall on Greece, rate concerns; US dollar dips'
    }, {
        'x' : datetime.datetime(2015, 6, 12),
        'title' : 'D',
        'text' : 'Zimbabwe ditches \'worthless\' currency for the US dollar '
    }, {
        'x' : datetime.datetime(2015, 6, 19),
        'title' : 'E',
        'text' : 'US Dollar Declines Over the Week on Rate Timeline'
    }, {
        'x' : datetime.datetime(2015, 6, 26),
        'title' : 'F',
        'text' : 'Greek Negotiations Take Sharp Turn for Worse, US Dollar set to Rally '
    }, {
        'x' : datetime.datetime(2015, 6, 29),
        'title' : 'G',
        'text' : 'Euro records stunning reversal against dollar'
    }, {
        'x' : datetime.datetime(2015, 6, 30),
        'title' : 'H',
        'text' : 'Surging US dollar curbs global IT spend'
    }]

H.add_data_set(data, 'line', 'USD to EUR', id = 'dataseries')
H.add_data_set(data2, 'flags', onSeries = 'dataseries',
                shape = 'circlepin',
                width = 16)

options = {
    'rangeSelector' : {
        'selected' : 0
    },

    'title' : {
        'text' : 'USD to EUR exchange rate'
    },
    'tooltip': {
                'style': {
                    'width': '200px'
                },
                'valueDecimals': 4,
                'shared' : True
            },

    'yAxis' : {
        'title' : {
            'text' : 'Exchange rate'
        }
    },

}

H.set_dict_options(options)

H.htmlcontent