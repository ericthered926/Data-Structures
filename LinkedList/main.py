import csv
import linkedlist_api

def main():
    print('working')
    output = open("output.txt","w")
    with open('data.csv') as csv_file:
        ll = linkedlist_api.LinkedList()
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[0] == 'CREATE':
                output.write(str(line_count) + ':' + str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + '\n')
                ll.__init__()
            if row[0] == 'DEBUG':
                output.write(str(line_count)+ ':' + str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + '\n')
                output.write(str(ll.debug_print()) + '\n')
            if row[0] == 'ADD':
                output.write(str(line_count)+ ':' + str(row[0]) + ',' + str(row[1]) + ',' + '\n')
                try:
                    print(row[1])
                    ll.add(row[1])
                except:
                    output.write(str(Exception) + '\n')
            if row[0] == 'SET':
                output.write(str(line_count)+ ':' +str(row[0]) + ',' + str(row[1]) + ',' + str(row[2])+ '\n')
                try:
                    ll.set(int(row[1]),row[2])
                except:
                    output.write(str(Exception) + '\n')
            if row[0] == 'GET':
                output.write(str(line_count)+ ':' +str(row[0]) + ',' + str(row[1]) + ',' + '\n')
                try:
                    ll.get(int(row[1]))
                except:
                    output.write(str(Exception) + '\n')
            if row[0] == 'DELETE':
                output.write(str(line_count)+ ':' +str(row[0]) + ',' + str(row[1]) + ',' + '\n')
                try:
                    ll.delete(int(row[1]))
                except:
                    output.write(str(Exception) + '\n')
            if row[0] == 'INSERT':
                output.write(str(line_count)+ ':' +str(row[0]) + ',' + str(row[1]) + ',' + str(row[2])+ '\n')
                try:
                    ll.insert(int(row[1]),row[2])
                except:
                    output.write(str(Exception) + '\n')
            if row[0] == 'SWAP':
                output.write(str(line_count)+ ':' +str(row[0]) + ',' + str(row[1]) + ',' + str(row[2])+ '\n')
                try:
                    ll.swap(int(row[1]),int(row[2]))
                except:
                    output.write(str(Exception) + '\n')
            line_count += 1
    output.close
main()

'''
*`CREATE` creates an instance of your array class.
* `DEBUG` prints the debug line to the console.
* `ADD` adds a value to the end of the array.
* `SET` sets a value at a given index in the array.
* `GET` retrieves a value at a given index in the array.  Your main program should print this value to the console.
* `DELETE` removes a value at the given index in the array.  Be sure to shift all elements down to fill the empty slot.
* `INSERT` inserts a value at the given index in the array.  Be sure to shift all elements up to make an empty slot.
* `SWAP` swaps two values at the given indices in the array.
'''