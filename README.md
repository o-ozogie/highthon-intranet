# highthon-intranet
2022 하이톤 인트라넷

## deployment
배포 이전에 `~/.aws/credentials`에 default profile에 대한 적절한 credential이 설정되어있어야 합니다.
```
# ~/.aws/credentials example
[default]
aws_access_key_id=AKIXXXXXXXXX
aws_secret_access_key=/ZyzXXXXXXXXXXXXXX
```
credential 설정 이후 아래 명령어를 실행하여 배포할 수 있습니다.
```
pip install -r requirements.txt
zappa deploy
```
로그는 다음 명령어로 확인할 수 있습니다.
```
zappa tail
```