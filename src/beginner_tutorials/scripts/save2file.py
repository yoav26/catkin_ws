
import csv


def create(array, name):

    with open(name, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # if os.stat('scores.csv').st_size == 0:
    #     writer.writerow([soil_types])
        writer.writerow(array)
    csvfile.close()



    '''with open('new.csv', 'a') as csvfile:
        csvfile.write(%f, %f, %f, (array[1], ) )'''


#create([2, 2, 2, 2, 2])

