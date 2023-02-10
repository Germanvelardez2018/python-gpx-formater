from jinja2 import Environment, FileSystemLoader






TITLE = "Drifter"
SUBTITULE ="I.N.T.I" 
NAME_FILE = "drifter.txt"


    


    



def date_formater(nmea_date):
    #print("date",nmea_date)
    y = nmea_date[0:4]
    m = nmea_date[4:6]
    d = nmea_date[6:8]
    h = nmea_date[8:10]
    m = nmea_date[10:12]
    s = nmea_date[12:14]
    return "%s-%s-%sT%s:%s:%sZ"%(y,m,d,h,m,s)


def get_gpx_format( nmea_file,title,subtitle):
    #Imprimo los datos sin procesar
    print("Datos a procesar:")
    elements_nmea = []
    for nmea in nmea_file:
        data = (nmea.split(','))[2:6]
        elements_nmea.append(data)
    print( 'Generando formato gpx...')
    env= Environment(loader=FileSystemLoader("gpx/"))
    template = env.get_template("gxp_format.xml")
    output = template.render(   t = title, 
                                st = subtitle,
                                nmea_list =elements_nmea ,
                                date = date_formater(elements_nmea[0][0]))
    with open('drfiter.gpx','w') as f:
        f.write(output)    




def main():
    with open(NAME_FILE,'r') as nmea_file:
        lines = nmea_file.readlines();
        data = []
        for nmea in lines:
            data.append(nmea[0:-1])
        print(data)
        get_gpx_format(data,TITLE,SUBTITULE)


if __name__ =='__main__':
    main()