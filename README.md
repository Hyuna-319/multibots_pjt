 멀티 로봇 namespace, Localization 적용
=============
멀티 로봇 시스템을 위해 로봇 별 namespace 및 Localization 적용



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

진행 내용
-------------

**1) mapping 깨짐 & map 범위 벗어남**
* 문제
  - turtlebot3 크기에 비해 큰 월드 & slam으로 인한 오차 누적
  - turtlebot3가 맵 범위 벗어남

<br>

* 해결 방안
  - 라이다 센서 감지범위 3.5 >> 10 m 확장
  - map.yaml의 origin [-2.52,-8.59,0] >> [-4.52, -8.59, 0]으로 맵 기준점 조정

<br>
<br> 

**2) urdf 네임스페이스 적용**
* 문제
   - 각 로봇마다 tf tree 생성을 위해 네임스페이스 적용 필요 

<br> 

* 해결 방안
   - 각 로봇의 urdf robot name prefix 적용
   - gazebo sensor plugin 추가
    
<br>
<br>

**3) 해결해야할 과제**
   - gazeibi_ros_ray_sensor 불러오기 실패로 bsae_link 및 관련 프레임 생성 불가 
   - turtlebot3 burger로 localization 실행가능하나 waffle에서 불가능한 점 


<br>
<br>

![KakaoTalk_20250217_164812658](https://github.com/user-attachments/assets/eda8bb99-2bc6-42dc-b5e2-68468839151f)


<img src="https://github.com/user-attachments/assets/1b1f3a38-bf87-4904-a4e9-772dc0eddf77" alt="ezgif-5-fa2ab96e05" width="500">


![image](https://github.com/user-attachments/assets/a7b69677-2386-4fe4-a847-90486d8d18c8)




