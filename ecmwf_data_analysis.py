from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

import json
import fiona
import numpy as np
from osgeo import gdal, gdalnumeric
from osgeo.gdalconst import GA_ReadOnly
import sys
gdal.UseExceptions()

def Usage():

    print("example run : $ python ecmwf_data_analysis.py country name")
    sys.exit(1)

def Shp_BBox(file_shp):

    ilVettore = fiona.open(file_shp)
    laProiezioneDelVettore = ilVettore.crs
    laBoundingBox = ilVettore.bounds

    return laProiezioneDelVettore, laBoundingBox

def fetch_ECMWF_data(file_output, time_frame, dict_area_richiesta):

    date = open(time_frame)
    time_frame_json = json.load(date)

    north = round(float(dict_area_richiesta['ymax'])*2/2)
    west = round(float(dict_area_richiesta['xmin'])*2/2)
    south = round(float(dict_area_richiesta['ymin'])*2/2)
    east = round(float(dict_area_richiesta['xmax'])*2/2)
    area_ecmwf_bbox = str(north) + "/" + str(west) + "/" + str(south) + "/" + str(east)

    print area_ecmwf_bbox

    # request WFP UN MESE ERA-Interim, Daily
    # server.retrieve({
    #     "class": "ei",
    #     "dataset": "interim",
    #     "date": time_frame_json,
    #     # "date": "1979-02-18/to/2014-02-25",
    #     "expver": "1931",
    #     "grid": "0.125/0.125",
    #     "levtype": "sfc",
    #     "param": "228.128",
    #     "step": "0",
    #     "stream": "mdfa",
    #     "area": area_ecmwf_bbox,
    #     "target": file_output,
    #     "time": "12",
    #     # "time": "00/06/12/18",
    #     "type": "fc",
    # })

    server.retrieve({
        "class": "ei",
        "dataset": "interim",
        "date": time_frame_json,
        # "date": "2016-04-25",
        "expver": "1",
        "grid": "0.125/0.125",
        "levtype": "sfc",
        "param": "228.128",
        "step": "24",
        # "step": "12/to/240/by/24",
        "stream": "oper",
        "area": area_ecmwf_bbox,
        "target": file_output,
        # "time": "00/06/12/18",
        "time": "12",
        "type": "fc",
    })

    return "Grib file generated in" + file_output + "\n"

def fetch_ECMWF_data_manuale(time_frame, dict_area_richiesta):

    date = open(time_frame)
    time_frame_json = json.load(date)

    north = round(float(dict_area_richiesta['ymax'])*2/2)
    west = round(float(dict_area_richiesta['xmin'])*2/2)
    south = round(float(dict_area_richiesta['ymin'])*2/2)
    east = round(float(dict_area_richiesta['xmax'])*2/2)
    area_ecmwf_bbox = str(north) + "/" + str(west) + "/" + str(south) + "/" + str(east)

    # IL TERZO GRIB SOMMA 10 GIORNI CON STEP 24 ORE
    # IL QUARTO GRIB SOMMA 10 GIORNI CON STEP 24 ORE E USA TIME A ZERO
    server.retrieve({
        "class": "ei",
        #"class": "od",
        "dataset": "interim",
        # "date": time_frame_json,
        # "date": "2016-04-25",
        "date": "2016-04-25",
        "expver": "1",
        "grid": "0.125/0.125",
        "levtype": "sfc",
        # "param": "228.128",
        "step": "24",
        # "step": "12/to/240/by/24",
        # "step": "0/to/240/by/240",
        "stream": "oper",
        "area": area_ecmwf_bbox,
        "target": "1_gribs_from_ecmwf/eth_ultimo_aprmay_2503.grib",
        # "time": "00/06/12/18",
        "time": "0",
        "type": "fc",
    })

    return "Grib file generated \n"

def fetch_ECMWF_46giorni(dict_area_richiesta):

    north = round(float(dict_area_richiesta['ymax'])*2/2)
    west = round(float(dict_area_richiesta['xmin'])*2/2)
    south = round(float(dict_area_richiesta['ymin'])*2/2)
    east = round(float(dict_area_richiesta['xmax'])*2/2)
    area_ecmwf_bbox = str(north) + "/" + str(west) + "/" + str(south) + "/" + str(east)

    # GRIB di 46 giorni
    server.retrieve({
        "class": "od",
        "dataset": "interim",
        "date": "2016-03-03",
        "expver": "1",
        "levtype": "sfc",
        "number": "1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50",
        "param": "8.128",
        "step": "1104",
        "stream": "enfo",
        "area": area_ecmwf_bbox,
        "target": "1_gribs_from_ecmwf/afr_46days.grib",
        "time": "00",
        "type": "pf",
    })

    return "Grib file generated \n"

def fetch_ECMWF_30giorni(dict_area_richiesta):

    north = round(float(dict_area_richiesta['ymax'])*2/2)
    west = round(float(dict_area_richiesta['xmin'])*2/2)
    south = round(float(dict_area_richiesta['ymin'])*2/2)
    east = round(float(dict_area_richiesta['xmax'])*2/2)
    area_ecmwf_bbox = str(north) + "/" + str(west) + "/" + str(south) + "/" + str(east)

    # GRIB di 30 giorni
    server.retrieve({
        "class": "od",
        "dataset": "interim",
        "date": "2016-03-03",
        "expver": "1",
        "levtype": "sfc",
        "number": "1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50",
        "param": "8.128",
        "step": "1104",
        "stream": "enfo",
        "area": area_ecmwf_bbox,
        "target": "1_gribs_from_ecmwf/afr_30days.grib",
        "time": "00",
        "type": "pf",
    })

    return "Grib file generated \n"

def apriRaster(raster):
    try:
        src_ds = gdal.Open(raster)
    except RuntimeError, e:
        print 'Unable to open raster file'
        print e
        sys.exit(1)

    return src_ds

def genera_statistiche_banda_grib(banda, indice):

    print
    print "DATA FOR BAND", indice
    stats = banda.GetStatistics(True, True)
    if stats is None:
        pass

    print "Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % (stats[0], stats[1], stats[2], stats[3])
    print "NO DATA VALUE = ", banda.GetNoDataValue()
    print "MIN = ", banda.GetMinimum()
    print "MAX = ", banda.GetMaximum()
    # print "SCALE = ", banda.GetScale()
    # print "UNIT TYPE = ", banda.GetUnitType()

def genera_gribs(file_date, area_bbox, raster_file):

    # date = open(file_date)
    # time_frame = json.load(date)
    # print time_frame
    # # proiezione, area_richiesta = Shp_BBox(vector_file)
    # area_richiesta = area_bbox
    # fetch_ECMWF_data(raster_file, time_frame, area_richiesta)
    pass

def genera_means(file_path, parte_iso, parte_date):

        print "ECMWF file exists calculating statistics"
        print "Change the name of the output grib file for fetching new data"
        nome_tif_mean = "2_mean_from_gribs/mean_" + parte_iso + parte_date + ".tif"

        ecmfwf_file_asRaster = gdal.Open(file_path)
        x_size = ecmfwf_file_asRaster.RasterXSize
        y_size = ecmfwf_file_asRaster.RasterYSize
        numero_bande = ecmfwf_file_asRaster.RasterCount

        # print "Ci sono %d bande " % numero_bande
        banda_esempio = ecmfwf_file_asRaster.GetRasterBand(1)
        type_banda_esempio = banda_esempio.DataType

        banda_somma = np.zeros((y_size, x_size,), dtype=np.float64)
        for i in range(1, numero_bande):
            banda = ecmfwf_file_asRaster.GetRasterBand(i)
            # NON MI SERVE IN QUESTA FASE MA E' UTILE IN PROSPETTIVA
            # genera_statistiche_banda_grib(banda, i)
            data = gdalnumeric.BandReadAsArray(banda)
            banda_somma = banda_somma + data

        # mean_bande_in_mm = (banda_somma/numero_bande)*1000
        # CONFRONTANDO FORECAST CON FORECAST NON HO BISOGNO DI AVERLO IN MILLIMETRI LASCIO TUTTO IN METRI
        mean_bande_in_mm = (banda_somma/numero_bande)

        # Write the out file
        driver = gdal.GetDriverByName("GTiff")
        raster_mean_from_bands = driver.Create(nome_tif_mean, x_size, y_size, 1, type_banda_esempio)
        gdalnumeric.CopyDatasetInfo(ecmfwf_file_asRaster, raster_mean_from_bands)
        banda_dove_scrivere_raster_mean = raster_mean_from_bands.GetRasterBand(1)

        try:
            gdalnumeric.BandWriteArray(banda_dove_scrivere_raster_mean, mean_bande_in_mm)
            return "Mean raster exported in" + nome_tif_mean + "\n"
        except IOError as err:
            return str(err.message) + + "\n"

def genera_means_ciclo10(file_path, parte_iso, parte_date, anni):


        print "ECMWF file exists calculating statistics"

        ecmfwf_file_asRaster = gdal.Open(file_path)
        x_size = ecmfwf_file_asRaster.RasterXSize
        y_size = ecmfwf_file_asRaster.RasterYSize
        numero_bande = ecmfwf_file_asRaster.RasterCount

        # print "Ci sono %d bande " % numero_bande
        banda_esempio = ecmfwf_file_asRaster.GetRasterBand(1)
        type_banda_esempio = banda_esempio.DataType

        # Write the out file
        driver = gdal.GetDriverByName("GTiff")

        conteggio = 0

        for anno in anni:
            print anno
            indice = anni.index(anno) + 1
            banda_somma_10gg = np.zeros((y_size, x_size,), dtype=np.float64)
            # nome_tiff_cumulata = "1_mean_from_gribs/mar01_mar11/cum_" + str(indice) + "_" + str(anno) + ".tif"
            # nome_tiff_average = "1_mean_from_gribs/mar01_mar11/avg_" + str(indice) + "_" + str(anno) + ".tif"
            nome_tiff_cumulata = "2_mean_from_gribs/apr25_may3/cum_" + parte_iso + "_" + str(indice) + "_" + str(anno)\
                                 + "_" + parte_date + ".tif"
            nome_tiff_average = "2_mean_from_gribs/apr25_may3/mean_" + parte_iso + "_" + str(indice) + "_" + str(anno)\
                                 + "_" + parte_date + ".tif"
            # print nome_tiff_average
            # print nome_tiff_cumulata
            print "Sto lavorando sull'anno %d" % anno
            for giorno in range(1, 11):
                numero_banda = conteggio + giorno
                # print giorno, anno
                banda = ecmfwf_file_asRaster.GetRasterBand(numero_banda)
                # genera_statistiche_banda_grib(banda, numero_banda)
                data = gdalnumeric.BandReadAsArray(banda)
                cumulata_10gg = banda_somma_10gg + data
                mean_10gg = (cumulata_10gg/10)

            raster_cum_from_bands = driver.Create(nome_tiff_cumulata, x_size, y_size, 1, type_banda_esempio)
            gdalnumeric.CopyDatasetInfo(ecmfwf_file_asRaster, raster_cum_from_bands)
            banda_dove_scrivere_raster_cum = raster_cum_from_bands.GetRasterBand(1)

            raster_mean_from_bands = driver.Create(nome_tiff_average, x_size, y_size, 1, type_banda_esempio)
            gdalnumeric.CopyDatasetInfo(ecmfwf_file_asRaster, raster_mean_from_bands)
            banda_dove_scrivere_raster_mean = raster_mean_from_bands.GetRasterBand(1)

            try:
                gdalnumeric.BandWriteArray(banda_dove_scrivere_raster_cum, cumulata_10gg)
                gdalnumeric.BandWriteArray(banda_dove_scrivere_raster_mean, mean_10gg)
                print "Raster calculated \n"
            except IOError as err:
                # return str(err.message) + + "\n"
                print str(err.message) + + "\n"

            raster_cum_from_bands = None
            raster_mean_from_bands = None

            conteggio += 1
            # conteggio += 11
            # print
        # print conteggio

def analisi_raster_con_GDALNUMERICS(grib_file):


    grib_file_aperto = gdal.Open(grib_file, GA_ReadOnly)

    x_size = grib_file_aperto.RasterXSize
    y_size = grib_file_aperto.RasterYSize
    numero_bande = grib_file_aperto.RasterCount

    for numero_banda in range(1, numero_bande+1):
        banda_corrente = grib_file_aperto.GetRasterBand(numero_banda)
        metadati = banda_corrente.GetMetadata()
        # if(metadati['GRIB_ELEMENT'] == 'TP'):
        #     print metadati

    return x_size, y_size, numero_bande

# if __name__ == '__main__':

    # if len(sys.argv) < 1:
    #     Usage()
    #     sys.exit(1)
    #
    # vector_file = "c:/sparc/input_data/countries/" + sys.argv[1] + ".shp"
    # paese = vector_file.split(".")[0].split("/")[-1]

    # ritornato = calculate_time_window_date.scateniamo_l_inferno(paese)
    # parte_date = ritornato.split("/")[1].split(".")[0][4:]
    # tre_lettere = vector_file.split(".")[0].split("/")[-1][0:3]
    # raster_file = "gribs/historical/" + tre_lettere + parte_date + ".grib"
    # print raster_file
    #
    # if os.path.isfile(raster_file):
    #     print "grib esiste"
    #     genera_means(raster_file)
    # else:
    #     print "grib non esiste"
    #     genera_gribs(ritornato, vector_file, raster_file)
    #     genera_means(raster_file)
    #

# FOCUS ON AFRICA
# dict = {'ymax': '40', 'xmin': '-20', 'ymin': '-40', 'xmax': '60'}
# dict = {'ymax': '38', 'xmin': '-26', 'ymin': '-35', 'xmax': '60'}
#
# # fetch_ECMWF_data("0_gribs_from_ecmwf/ellolo.grib", 'dates/req_2607_02_03_19792015.txt', dict)
#

# fetch_ECMWF_data_manuale('dates/req_2231_03_19792016.txt', dict)

# fetch_ECMWF_data_manuale('dates/req_1524_03_19792016.txt', dict)
# fetch_ECMWF_46giorni(dict)

#
# grib_file = "0_gribs_from_ecmwf/historical/afr_s24_th12_mar_2131.grib"
# grib_file = "0_gribs_from_ecmwf/historical/afr_s24_th12_mar_2231_240.grib"

# grib_file = "frcst_46gg_21Mar.grib"
# numero_bande = analisi_raster_con_GDALNUMERICS(grib_file)[2]

# for numero_banda in range(1, numero_bande):
#     print "Sto lavorando sulla banda %d" % numero_banda
#     grib_file_aperto = gdal.Open(grib_file, GA_ReadOnly)
#     banda = grib_file_aperto.GetRasterBand(numero_banda)
#     genera_statistiche_banda_grib(banda, numero_banda)

# print numero_bande

# raster_file = "0218_0225.grib"
# genera_means(raster_file, "fji", "1825_02_19792015")
#anni = []
#for anno in range(1979, 2016):
#      # if anno != 2012:
#      anni.append(anno)
#
# print anni
# # print len(anni)
#

#grib_file = "0_gribs_from_ecmwf/historical/BurDjiEriEthSomSouUgaRwaTan_2706_04_05_19792016.grib"
#genera_means_ciclo10(grib_file, "eas_afr", "2503_0405_19792015", anni)
# fetch_ECMWF_data_manuale('dates/req_2505_0405_19792016.txt', dict)