import numpy as np

def haverSine(latA, lonA, latB, lonB):
    """Calcula a distancia em METROS
    
    Entre dois pontos A e B com
    LATitude e LONgitude
    
    Returns:
        [floar] -- [Distancia em metros]
    """
    

    latA,lonA, latB,lonB = map(np.radians,[latA,lonA, latB,lonB])

    dLat = latB - latA
    dLon = lonB - lonA

    a = np.sin(dLat/2.0)**2 + \
        np.sin(dLon/2.0)**2 * \
        np.cos(latA) * np.cos(latB)
        
    
    c = 2 * np.arctan2(
        np.sqrt(a), np.sqrt(1-a)
    )

    d = 6378160 * c
    return d



if __name__ == '__main__':

    pscCompA = [-22.973870, -43.387209]
    pscCompB = [-22.974320, -43.387207]
    pscLargA = [-22.974102, -43.387241]
    pscLargB = [-22.974095, -43.387001]

    print('hsin C',haverSine(pscCompA[0],pscCompA[1],pscCompB[0],pscCompB[1]))


    print('hsin L',haverSine(pscLargA[0],pscLargA[1],pscLargB[0],pscLargB[1]))
