import cv2, pafy

# 동영상 URL
url = "https://www.youtube.com/watch?v=YkEt1bbVH8c"

# connection
video = pafy.new(url)

# 정보 출력
print('title=', video.title)
print('video.rating=', video.rating)

# 유튜브 동영상 캡쳐 준비
best = video.getbest(preftype='mp4')
cap = cv2.VideoCapture(best.url)

while(True):
    # 동영상에서 캡쳐 - retval은 이미지 존재여부이고 frame 이 영상
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame', frame)

    # 흑백으로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 경계선 검출
    edges = cv2.Canny(gray, 100, 100)
    cv2.imshow('edges', edges)

    key = cv2.waitKey(25)
    # esc를 누르면 재생 중지
    if key == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

