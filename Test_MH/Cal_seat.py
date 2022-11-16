max_row_seat = 8
max_colum_seat = 4

def convert_data():
    with open("C:/Users/suwan/plain.txt") as f:
        lines = f.readlines()
    list_booked = []

    for i in lines:
        list_booked.append(i[0]+i[1])
        print(i)
    list_all_seat=[]
    for i in range (0,max_colum_seat+1):
        list_seat= []
        for j in range(1,max_row_seat+1):
            booked=False
            if chr(i+65)+str(j) in list_booked:
                booked = True
            list_seat.append(booked)
        list_all_seat.append(list_seat)
    return list_all_seat
    
def cal_seat(booking):
    list_all_seat= convert_data()
    list_booking = []
    for i in range(0,len(list_all_seat)):
        for j in range(0,len(list_all_seat[i])):
            seat_booking  = []
            for k in range(j,len(list_all_seat[i])):
                if list_all_seat[i][k] ==False:
                    seat_booking.append(chr(i+65) + str(k+1))
                    if len(seat_booking) == booking:
                        if seat_booking not in list_booking :
                            list_booking.append(seat_booking)
                        seat_booking = []
                    if k ==3 and ( booking - len(seat_booking) ==1  or len(seat_booking)==1 ) and j<=4   :
                        seat_booking =[]
                if list_all_seat[i][k] ==True:
                    
                    seat_booking = []
                    break
    return list_booking 

