
def BinarySearch(arr,elem):
    if len(arr) == 0 or elem < arr[0]:
        return 0
    left = 0
    right = len(arr)
    while left + 1 < right:
        n = (left + right) // 2
        if elem >= arr[n]:
            left = n
        else:
            right = n 
            
    return right




def Classify(ori_arr,x,y_of_x):
    
    len_ = len(ori_arr)
    for index in range(len_):
        value = ori_arr[index]
        new_list = []
        while (ori_arr[index][0] == value[0]):   
            new_list.append(ori_arr[index][1]) 
            
            if index == len_ - 1:
                break 
                
        x.append(value[0])
        y_of_x.append(sorted(new_list))

            
            

def StoreIndice(y_of_x,all_y,indice_list):
        len__ = len(all_y)
        for index in range(len(y_of_x)):
            another_len = len(y_of_x[index])
            for i in range(len__ + 1):
                if i == len__:
                    indice_list[index][i] = another_len
                    break 
                elem =  all_y[i]
                the_list = y_of_x[index]
                
                if elem <= the_list[0]:
                    indice_list[index][i] = 0  
                elif elem > the_list[-1]:
                    indice_list[index][i] = another_len 
                else:
                    for j in range(another_len):
                        if elem <= the_list[j]:
                            indice_list[index][i] = j
                            break
            

            
            
class Solution(object):

    def __init__(self, points):
        self.points = points
        self.store_x = []
        self.store_y_of_cor_x = []
        
        self.points.sort(key=lambda x: x[0])
        self.all_y = [x[1] for x in self.points]
        self.all_y.sort()
        self.index_info = []
        Classify(self.points,self.store_x,self.store_y_of_cor_x)  
        for j in range(len(self.store_y_of_cor_x)):
            y = [0  for i in range(len(self.all_y) + 1)]
            self.index_info.append(y)    
            
        StoreIndice(self.store_y_of_cor_x,self.all_y,self.index_info)
        



    def query(self, rect) -> int:
        count = 0
        left_most  = rect[0][0]
        right_most = rect[0][1]
        lower_most = rect[1][0]
        upper_most = rect[1][1]
        x1 = BinarySearch(self.store_x,right_most)
        x0 = BinarySearch(self.store_x,left_most - 1)
        initial_loop = True      
        for i in range(x0,x1): 
            if (initial_loop):
                y1 = BinarySearch(self.all_y,upper_most)
                y0 = BinarySearch(self.all_y,lower_most - 1)
                save_y0  = y0
                save_y1 = y1
                y1 = self.index_info[i][y1]
                y0 = self.index_info[i][y0]
                initial_loop = False
            else:
                y1 = self.index_info[i][save_y1]
                y0 = self.index_info[i][save_y0] 
            count += (y1 - y0) 
            
        return count


if __name__ == "__main__":
    points = [[1, 1], [3, 3], [2, 2], [1, 3]]
    sol = Solution(points)
    print(sol.query([[1,3], [1,3]]))
    print(sol.query([[1,5], [2,5]]))
