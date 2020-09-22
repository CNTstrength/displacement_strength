import cv2

def show_movie(file_name):
    img_size = 2

    output_file = "./output/output.wmv"
    cap    = cv2.VideoCapture(file_name)
    fps    = cap.get(cv2.CAP_PROP_FPS)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    fourcc = cv2.VideoWriter_fourcc(*'WMV1')
    out    = cv2.VideoWriter(output_file, int(fourcc), fps, (int(width*img_size), int(height*img_size)))
    count = 0
    telop_height = 50
    sq_binary = 255


    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.GaussianBlur(frame,(3,3),0)
            __,frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            frame = cv2.bitwise_not(frame)
            frame = cv2.resize(frame, (int(width*img_size), int(height*img_size)), interpolation = cv2.INTER_LANCZOS4)
            font = cv2.FONT_HERSHEY_SIMPLEX
            time_print = str(round(count/fps, 1)) + " [sec]"
            cv2.putText(frame, time_print, (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (sq_binary, sq_binary, sq_binary), thickness=2)
            cv2.imshow('frame',frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            out.write(frame)
            count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite('./view/sample.png', frame)
                break
        else:
            break


if __name__ == '__main__':
    file_name = "./wmvfile/test.wmv"
    show_movie(file_name)
