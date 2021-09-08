# Computer System
## 연산장치 vs 기억장치
### 폰노인만 구조
* 연산장치와 기억장치는 분리되어 있으며, 연산장치는 기억장치에서 데이터를 로딩해서 처리 후, 다시 기억장치로 가져다 놓는다.
* 하지만 사람은 연산 및 기억장치가 분리되어있지 않다.
* CPU와 Memory. 거의 대부분의 OS의 기능을 Memory 관리에 집중한다.

### System BUS
1. 두 Device 연결된 전선 (데이터 이동 통로)
2. 통신 규약 

### 연산장치
* 어떤 Input 들어왔을 때 Output 내준다.
* 병렬 처리
* CPU, Graphic card 

### 기억장치
* 일정한 기간동안 정보 유지하고 있다.
* Memory: DRAM, HDD, SSD (같은 기능을 한다.)
* 모든 메모리들이 정보 기억 및 저장하고, 내가 그 정보를 기억, 수정, 삭제 가능하다.

### CPU
* OS 관점에서 CPU는 신경쓰지 않아도 된다. 시키는 일만 처리를 한다. (like 자판기)

## 기억장치의 종류
### Memory
* 정보(프로그램과 데이터)를 담는다. Memory는 CPU에 정보를 전달해서 동작한다. 
* DRAM (Main memory): CPU에 명령과 데이터 직접 전달한다. 빠르다. 전원 꺼지면 정보 사라진다. 휘발성.
* SSD (Secondary) : CPU와 직접 만나지 못 한다. 비록 느리지만 전원이 꺼지더라도 정보 계속 남아있다. 비휘발성.
* disks (Secondary) : 요즘에는 많이 쓰지 않는다. 
* 정반대의 특성이 상호보완적이다.
* Booting : SSD내에 Windows가 SSD -> DRAM -> CPU 한 줄 한 줄 실행되는 것. But 처음 위치 알려주는 것 필요 (Bootstrap)

### DRAM
* Dynamic Random Access Memory
* DRAM : 어떤 정보를 저장하기 위해서는 계속 충전을 해줘야 한다. 속도가 SRAM에 비해 느리다.
* SRAM (Static) : 충전을 해 주지 않아도 저장 가능, 회로 더욱 복잡. 비용이 더 비싸다.

### Caching
* 자주 쓰는 데이터만 DRAM에 옮겨서 CPU와 Direct로 연결시켜 효율을 높이는 것이 Caching concept이다.

