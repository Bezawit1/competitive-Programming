class Solution(object):
    def averageWaitingTime(self, customers):
        total_time = customers[0][0] + customers[0][1] 
        wait_time = total_time - customers[0][0]
        print( wait_time , total_time , customers[0][0])
        for i in range (1,len(customers)):
            if total_time< customers[i][0]:
                total_time = customers[i][0]
            total_time += customers[i][1]
            wait_time += (total_time - customers[i][0])
            print( wait_time , total_time , customers[i][0])
        print(wait_time , len(customers))
        avg = float(wait_time)/len(customers)
        return avg




        