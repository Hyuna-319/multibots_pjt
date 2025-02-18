 멀티 로봇 namespace, Localization 적용
=============
멀티 로봇 시스템을 위해 로봇별 namespace 및 Localization 적용한 프로젝트



[프로젝트 기록](https://velog.io/@cherry0319/%EB%8B%A4%EC%A4%91-%EB%A1%9C%EB%B4%87-%EC%8B%9C%EC%8A%A4%ED%85%9C-vry0vpjw) 

<br>


인원 및 기간
-------------
* 1명 [김현아](https://github.com/Hyuna-319)
* 2025.01.25 ~ 2025.02.17
  
<br> 

사용 기술
-------------
* Language : Python3
* OS : Linux Ubuntu 22.04 jammy
* Skills : ROS2 Humble Rviz2, Nav2, SLAM, Turtlebo3 waffle 

  
<br>

참고
-------------

* [AI, Deep Learning and Robotics](https://robotics.snowcron.com/robotics_ros2/multi_bot_03_launch.htm)
* [turtlebot3_multi_robot](https://github.com/arshadlab/turtlebot3_multi_robot)
* [turtlebot3 github](https://github.com/ROBOTIS-GIT/turtlebot3)

<br>
<br>

진행 내용
-------------

**1) mapping 깨짐 & map 범위 벗어남**
* 문제점
  - turtlebot3 크기에 비해 큰 월드 & slam으로 인한 오차 누적
  - turtlebot3가 맵 범위 벗어남

<br>

* 해결 방안
  - 라이다 센서 감지범위 3.5 >> 10 m 확장
  - 매핑이 부족한 픽셀은 gimp로 수정 
  - map.yaml의 origin [-2.52,-8.59,0] >> [-4.52, -8.59, 0]으로 맵 기준점 조정

<br>
<br> 

**2) urdf 네임스페이스 적용**
* 문제점
   - 각 로봇마다 tf tree 생성을 위해 네임스페이스 적용 필요 

<br> 

* 해결 방안
   - 각 로봇의 urdf `robot name` prefix 적용
   - gazebo sensor plugin 추가
   - package.xml에 pacakge dependencies 추가 
    
<br>
<br>


결과
-------------

* 3대 로봇의 tf tree 생성완료
* localization 적용 및 정상 작동 확인

<br>
<br>


### 실행 결과 이미지

<br>

![image](https://github.com/user-attachments/assets/e1b78df0-e6f8-4ffb-949e-689c9eeee914)

![image](https://github.com/user-attachments/assets/fbda7d83-e934-4556-94d3-75f93cdd590e)



![image](https://github.com/user-attachments/assets/4e3b388e-17f0-4b4d-987b-f854d7524b6b)

