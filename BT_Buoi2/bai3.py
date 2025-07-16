tuoi = int(input("Tuổi của bạn là : "))
if( tuoi < 12 ) :
    print("Trẻ con")
elif( tuoi < 18 and tuoi >= 12 ) :
    print("Thiếu niên")
else :
    print("Người lớn")