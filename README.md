KUAL 레퍼지토리 사용법(꼭 읽어주세요)
===================================

# 해당 설정 방법은 Git Bash를 이용한 방법입니다.


### 1. 현재 화면 오른쪽 상단에 fork를 합니다.
<br>

![image](https://user-images.githubusercontent.com/83203154/227473488-ebdab66f-c9d1-45db-a140-e7da01b3097a.png)

### 2. 레퍼지토리 복사가 된 것을 알 수 있습니다.
<br>

![image](https://user-images.githubusercontent.com/83203154/227473802-83863607-c502-4bb0-bddb-f58d3c9cd5ee.png)




### 3. 로컬저장소를 만들기 위해 바탕화면에 임의적인 이름의 폴더를 만듭니다.
![image](https://user-images.githubusercontent.com/83203154/227699750-fe958813-25e4-4fb8-901d-8434cd5e926f.png)





### 4. 아까 전 2번 과정, fork를 통해 레퍼지토리를 복사를 하였습니다. 해당 레퍼지토리의 url을 복사합니다.

![image](https://user-images.githubusercontent.com/83203154/227700133-8035eb8a-a3b1-42d1-a8be-ce7435b213e5.png)





### 5. Git Bash을 실행하여 3번과정에서 자신이 만든 파일의 위치로 이동하고 git clone [아까 복사해두었던 url] 을 입력합니다.
#### ※주의 : 그림에서 보여지는 저의 레퍼지토리 url과는 달라야합니다. 자신의 레퍼지토리 url을 사용하셔야 합니다.


![image](https://user-images.githubusercontent.com/83203154/227700415-3c7bb71c-64f4-4b0c-a002-fdf034b66115.png)



### 6. 그러면 TA-Algorithm 이라는 폴더가 생기며, 폴더 안에는 .git이라는 폴더와 현재 보고있는 가이드 라인 README.md 파일이 생성이 될 것입니다.


![image](https://user-images.githubusercontent.com/83203154/227700614-a71214a5-f3ca-428f-bfd0-8e27daf4e67d.png)

![image](https://user-images.githubusercontent.com/83203154/227701308-56a39738-2c38-4d34-884f-5d2c742d0b38.png)


### 7. git remote -v를 실행시키면 현재 연결되어 있는 원격저장소를 나타내는 것인데 Origin은 자신의 원격저장소이며, 그 다음에 추가 할 것은 그룹 원격저장소를 추가할 것입니다.
### 그룹 원격 저장소를 추가하기 위해 git remote add upstream https://github.com/Algorithm-Club-KUAL/TA-Algorithm.git 을 작성하세요

![image](https://user-images.githubusercontent.com/83203154/227701200-f5edfbee-e5ec-4f34-ae0e-178c4bd6a07f.png)

![image](https://user-images.githubusercontent.com/83203154/227701003-1eaf0caa-9026-4b29-95d0-6404e9d7b899.png)



# 앞으로 어떤 식으로 진행되는지에 대한 개략도입니다.

![image](https://user-images.githubusercontent.com/83203154/227704123-347f42b1-4f97-44a8-a691-3095644568d9.png)

### 위 그림의 순서
#### 1. fork를 통해 upstream의 레퍼지토리를 origin으로 복사하였습니다. (위의 내용을 진행하였다면 이 부분은 신경 쓰지않아도 됩니다.)
#### 2. local과 origin, upstream과의 관계를 만들기 위해 git bash의 커맨드라인에 git remote add origin or upstream을 입력하였습니다.
#### 3. 여기서부터 중요합니다. git fetch upstream ( 뜻 : Git에서 fetch는 원격 저장소에서 반영된 내용을 받아 올 때 사용하는 명령어입니다. 즉 여러분께서 알고리즘 문제를 그룹 레퍼지토리에 올릴때마다 업데이트가 되는 것인데 이 업데이트 내용을 자신의 로컬저장소의 버전을 맞추기 위해 진행하는 것 입니다.)
![image](https://user-images.githubusercontent.com/83203154/227702285-756f88a7-d76f-4539-a5f1-7a033c4be6eb.png)

#### 4. 패치된 내용을 받아왔으면,  merge를 통해 main (git bash에서 보면 됨) 병합합니다. 만약에 자신이 main이 아니고 master일시 git branch -M main을 타이핑하여 master를 main으로 고쳐주세요.(현재 로컬저장소가 main이 메인 브랜치이기 때문에 master가 생기면 곤란하게 됩니다.)
![image](https://user-images.githubusercontent.com/83203154/227702352-fbf97899-4532-4a99-8d3f-f6ac7a3c7b0a.png)
![image](https://user-images.githubusercontent.com/83203154/227702401-2cd078ab-3b82-4706-be05-c5889ff6b86b.png)
#### tips : upstream/ 작성후 탭키를 누르면 자동완성됩니다.  여기서 upstream/main은 fetch를 통해 받아온 업데이트 정보를 담고 있는 원격 저장소의 브랜치라고 보면 됩니다.

#### 5. 그룹 원격저장소와 로컬 저장소와의 동기화(fetch와 merge)가 완료되면, 앞으로 알고리즘 내용을 이름 별로 관리하기 위해서 디렉토리를 생성합니다.(ex : git bash 커맨드라인에서 mkdir SM이나 SM폴더 생성)
#### ※주의 : CSM(시문)은 제 이름의 약자이며 자신의 이름 약자를 적어야합니다. 만약에 초성이 겹쳐 이미 폴더가 존재할 경우 구분지어서 만들어 주세요.
![image](https://user-images.githubusercontent.com/83203154/227702860-512843e1-8395-4e5c-b8a7-e45a29f48131.png)
#### 6. git add . 을 해서 로컬에서 추가한 폴더를 stage 영역으로 올린다.
![image](https://user-images.githubusercontent.com/83203154/227703268-4f7ae06f-9057-4347-a30e-46aeb6b6cd54.png)
#### 7. git commit -m "이름 폴더 생성"
![image](https://user-images.githubusercontent.com/83203154/227703344-d31d5190-00de-46f5-bc2f-8eec07963bd9.png)
#### 8. 마지막으로 그룹 원격 저장소와 자신의 원격 저장소에 올리기.
![image](https://user-images.githubusercontent.com/83203154/227703427-7bf341cf-cbb4-4e10-9656-2e8b2e19dfc7.png)

![image](https://user-images.githubusercontent.com/83203154/227703527-b9ce756b-cfe4-4fa3-9f6d-2445d6e1c8b7.png)


#### 만약에 자신의 원격저장소 git push origin main에서 아래와 같은 에러가 뜬다면 현재 로컬저장소와 자신의 원격저장소가 동기화 된 것이 아니기 때문에
git fetch origin을 하고 git merge origin/main을 작성해주어 동기화를 시켜줘야 합니다.
![image](https://user-images.githubusercontent.com/83203154/227704291-72be89f8-ecff-4d72-97fc-fb82a6bb1932.png)

![image](https://user-images.githubusercontent.com/83203154/227704413-449d6d45-094d-4b2b-b66c-945c5af0e56e.png)




#### 9. 확인하기
![image](https://user-images.githubusercontent.com/83203154/227704187-f05fbf46-1c50-4459-a97e-7ef4041bf7a3.png)





## README 수정/ 2023-03-25 ver 작성자 : 천시문
추후 각 개인 브랜치를 통해 병합하는 과정 설명 예정입니다.













