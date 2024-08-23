git checkout main

git pull

git branch 學號

git checkout 學號

git add .

git commit -m"更新內容敘述"

git push

git push --set-upstream origin 41123119

git branch -d 學號

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

更新順序

先轉到主分支(git checkout main)

將他人更新分支下載(git pull)

建立分支(git branch 學號)

從主分支轉換到分支(git checkout 學號)

將本地資源上傳

git add .

git commit -m"更新內容敘述"

第一次使用或要更改位推送分支

git push -u origin 學號

後續幾次若要更新到同樣分支只需(git push)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

刪除分支git branch -d 學號(分支名稱)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Download

1.下載 git 參考 https://www.youtube.com/shorts/JsSmJhCi8-I?feature=share

2.在桌面新增 new folder

3.用滑鼠右鍵點folder 後 open git bash here

4.在bash 輸入git init

5.git clone --recurse-submodules https://github.com/QIU0908/2407024-nfu-ComforMitt.git

git config --global user.name "John Doe"

git config --global user.email "johndoe@example.com" (與github 一樣)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Branch 1.在bash 輸入 git branch 先確定有main or master

2.如果沒有在folder中任意修改一字

3.後git add .
ls(顯示你修改的文件)

4.git branch 後因該有main or master

5.後 git branch 學號

6.git checkout 學號 (轉到分支)

7.git commit -m"XXXX"

8.git push -u origin (學號) ( 第一次上傳)以後git push 就好

9.在github頁面合併

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

下次記得先 git checkout main 後git pull
