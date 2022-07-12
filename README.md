<div align="center">

<img src="https://user-images.githubusercontent.com/60145951/158914541-46bae0c2-28f7-46d7-80f4-6a7cb3e15579.png" width=50><br>

<h3>HUFSALGO</h3><br>

<a href="https://github.com/hufslion10th/HUFSALGO/issues">
<img src="https://img.shields.io/github/issues/hufslion10th/HUFSALGO?color=0088ff&style=for-the-badge&logo=github" alt="@HUFSALGO's issues"/></a>
<a href="https://github.com/hufslion10th/HUFSALGO/pulls">
<img src="https://img.shields.io/github/issues-pr/hufslion10th/HUFSALGO?color=0088ff&style=for-the-badge&logo=github" alt="@HUFSALGO's pull requests"/></a>

</div>

# 커밋 컨벤션

[git commitizen의 사용법 알아보기](https://blog.dnd.ac/github-commitzen-template/)를 참조하여 작성합니다.

1. `node.js`를 설치합니다.
2. 아래 명령어를 실행합니다.

```sh
npm install -g commitizen
npm install -g cz-conventional-changelog
npm install -g cz-emoji-conventional cz-emoji
echo '{ "path": "cz-emoji-conventional" }' > ~/.czrc
```

3. 파일 변경사항 적용 후 `git commit -m "메세지"`가 아닌 `git-cz` 명령어를 실행하여 커밋을 올립니다.
