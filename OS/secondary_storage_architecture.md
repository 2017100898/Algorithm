# Secondary-Storage Architecture
## Secondary Storage
* DRAM을 제외하고 시스템 바깥에 있는 Storage를 뜻한다.
* 특징
	* 100기가 이상
	* cost 가 저렴하다
	* persistent하다 (data survives power loss)
	* 느리다
* Disks and the OS
	* Disk 는 매우 많은 에러가 일어나지만 OS가 내부적으로 다 처리한다.
	* Disk 단위는 Platter, 그 표면은 surface, 정보 기록할 수 있는 동심원을 track, track을 일정한 단위로 구분을 지으면 sector, track의 집합을 cylinder 라고 한다.
* Disk Performance
	* Seek (탐색)  : disk arm이 물리적으로 움직여서 다른 track (또는 cylinder)을 읽는 것, arm이 움직이는 시간 동안은 트랙을 읽을 수 없기 때문에 지연이 발생한다.
	* Rotation (회전) : 어떤 sector가 축을 중심으로 회전하는 것, 회전하는 동안에도 마찬가지로 지연이 발생한다.
	* Transfer : 데이터를 전송하는 시간
* Disk Scheduling
	* 어떤 순서로 프로세스를 실행하면 성능이 좋아지는가?
	
## Disk Scheduling
* OS는 같은 시간 동안 최대한 많은 일을 하는 것이 목적이다.
1. Arm의 움직임을 가장 효율적으로 하자. 즉, Seek time을 줄여보자.  `대부분 Seek time을 줄이기 위한 알고리즘을 사용한다.`
2. Rotational latency는 sector가 arm으로 돌아오는 시간을 뜻하고, 이것을 줄이는 방법도 있다.
* Minimize seek time : Seek time == Seek distance
	* Disk bandwidth : 시간 안에 얼마만큼의 데이터가 이동했는지를 측정하는 것 `(first request ~ final request bytes) / time`

### Example
* Cylinder number  : 98, 183, 37, 122, 14, 124, 65, 67
* Cylinder는 가장 안쪽에 있는 것이 0번이고 바깥으로 갈 수록 커지도록 넘버링 한다.
* Head pointer : 현재 head 가 있는 위치
* 어떤 순서로 요청을 해야 arm의 움직임을 최소화할 수 있을 것인가?

### FCFS
* 98, 183, 37, 122, 14, 124, 65, 67 순서대로 arm 을 움직이는 방법이다.
* 이 경우 움직인 총 거리는 640 Cylinder가 된다.
* 가장 구현하기 쉽고 단점이 많다. 즉 시간이 많이 걸린다.
* 동일한 request가 있을 때 arm의 움직임을 줄일 수 있는 방법은?

### SSTF (Shortest Seek Time First)
* 현재 위치에서 가장 조금 움직일 수 있는 위치로 이동하는 방법이다.
* starvation이 발생할 수 있다.
* 위 예제에 따르면 236 Cylinder를 이동하게 된다. (FCFS에 비해 줄어듦)

### SCAN (elevator algorithm, 양방향)
* 처음에는 왼쪽으로 계속해서 가다가, 끝에 도달하면 반대 방향으로 끝까지 가는 알고리즘이다. 중간에 새로운 것이 들어와도 다시 돌아가지 않는 것이 특징이다.
* 208 Cylinder

### C-SCAN (Circular SCAN, 단방향)
* 무조건 한 방향으로만 가는 방법이다. 끝에 도달하면 처음부터 같은 방향으로 끝까지 간다.

### C-LOOK (단방향)
* Look은 SCAN과 다르게 **끝까지 가는 것이 아닌** 현재 내가 가야하는 최솟값 부터 최댓값까지만 왔다갔다 하는 방법이다.

## RAID (Redundant Array of Independent Disks)
* RAID는 여러 개의 Disk를 묶어서 하나의 Volume으로 만들어서 사용하는 방법이다. 여러 개를 하나의 Disk처럼 사용할 수 있다.
* 하나의 RAID Controller는 모든 디스크를 다 관리한다.

### RAID의 장점
* Reliability via Redundancy `Reliability : Disk 에러 관련 안정성`
	* **Mirroring** : 같은 데이터를 여러 Disk에 동시에 저장하는 것을 뜻하고, Mirroring을 통해 안정성을 높일 수 있다.
		* MTTF (Mean time to failure, 평균 무고장 시간) : single disk일 때 11년이라면, mirrored disk system을 구축하면 무고장 시간이 제곱 (100,000^2/(2*10)) 되어서 57,000 년이 된다. 
	* Mirroring 시 쓸 때는 속도가 똑같지만 읽을 때 속도 차이가 발생한다.
* Performance via Parallelism
	* **Data Striping** : Disk마다 별도의 controller가 있다. controller를 통해 각 디스크에 데이터를 나눠서 동시에 저장하는 것을 뜻한다.
	

### RAID0 (Striping only)
* 여러 개의 디스크 모두 Striping 하는데 사용하는 방식을 뜻한다.
* 어떤 데이터가 있으면 그 데이터를 n개로 잘라서 동시에 저장하고 읽을 때도 각각 동시에 읽는다. 이러한 방식은 매우 성능이 빠르다.
* 다만, 디스크는 Data의 Persistant는 매우 중요한데 디스크 중 하나가 고장나면 모든 디스크에 있는 데이터를 사용하지 못 한다는 단점이 존재한다.

### RAID1 (RAID0과 반대되는 개념, Mirroring only)
* Striping 하지 않고 미러링만 하는 방식, 어떤 데이터가 들어오면 n 개의 디스크에 모두 다 복사한다. 하나가 없어져도 에러가 발생하지 않기에 안정적이다.
* 저장 공간을 반 밖에 사용하지 못 한다는 단점이 있다. 절반은 Mirroring 하는데 사용한다.

#### RAID2
* Hamming Code ECC (Error correcting codes)
* 비트 단위로 Hamming code를 따로 저장하면 에러 발생 시 에러 검출 및 복구를 할 수 있다. 
* 데이터를 잃어버렸을 때 이를 복구할 수 있는 코드를 저장하는 것이다. 데이터 전체를  복제하면 저장 공간이 많이 소비되기 때문.

#### RAID3
* Parity Bit 를 사용하는 방법이다.
* 특정 바이트를 읽고 싶을 때, 다른 디스크에서 읽으면 빠르긴 하지만 각각 Seek time이 소요된다.  (바이트가 여러 개의 디스크에 분산되어 있기 때문)

#### RAID 4
* 블럭 단위로 저장하는 방법이다.
* Parity를 체크하는 디스크가 별도로 필요하다. 블럭 단위로 Parity의 값을 받는다. Block 단위로 저장이 되어있기 때문에 A seek time 만 소요되고, B, C는 그 옆에 있다.
* Parity 값은 앞선 디스크들의 값을 연산하여 나온 값이므로 그 중 한 값만 변해도 Parity 값이 변하는 단점이 있어서 RAID4 또한 사용하지 않는다.

### RAID5 
* RAID5는 자주 사용되는 방법이다.
* Parity를 특정한 디스크에서 전담하는 것이 아닌 여러 디스크가 번갈아가면서 배치하는 것을 뜻한다.
* Disk 1개가 고장나더라도 복구 가능하다는 장점이 있다.

### RAID6
* Parity 를 2군데 놓는 방법이다.
* Disk 가 두 개가 고장나더라도 복구를 할 수 있다.
* 공간 효율성은 떨어진다.

### RAID 0+1
* Striping 으로 구성 후 그 두 개를 Mirroring 하는 방법이다.
* R0 : disk 1개가 오류나면 멈춘다.
* R1 : 오류 복구 시 복사를 한다.
* RAID0+1은 하나가 고장나면 디스크 반절을 사용하지 못 한다.

### RAID 1+0 (or RAID10)
* Mirroring으로 구성한 RAID 들을 Striping으로 붙이는 방법이다.
* RAID0+1은 하나가 고장나면 해당 디스크만 사용하지 못 한다.

## Direct Attached Storage (DAS)
* DAS는 클라이언트들이 서버에만 접근할 수 있고, 서버 뒷쪽에 Storage가 있는 것을 뜻하며, 클라이언트는 Storage에 직접 접근할 수 없고 서버에 요청을 해야 한다.

## Network Attached Storage (NAS)
* NAS는 클라이언트들이 네트워크를 통해서 공유 디스크를 사용하는 것이다.








