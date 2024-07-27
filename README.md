# CIE
Citizens' Internet Exploerer 公民浏览器

## 目录

- [简介](#简介)
- [构想](构想)
- [安装](#安装)
- [贡献](#贡献)
- [许可证](#许可证)
- [致谢](#致谢)

## 简介  

Citizens' Internet Exploerer 公民浏览器，旨在帮助用户保护浏览隐私，主要为反贼群体设计。  

浏览器关闭时将数据上传到服务端并清空本地数据，下次启动时须手动指定服务端ip并输入密码鉴权，从服务端获取浏览数据。  

每次关机前及时运行TRIM指令并配合BitLocker，可有效防止共匪特务设备审查。  

## 构想  

√密码鉴权  

√自动同步  

√客户端关闭自动销毁  

√服务端密令自动销毁  

√密码错误三次自动销毁  

-HTTPS支持  

-嵌入FireFox实现真·开箱即用  

-一键脚本或一键安装包降低技术门槛  


## 安装  

### 先决条件  

- 客户端依赖Python3（建议3.10及以上）
  
- 服务端依赖Node
  

### 步骤  

1. 服务端：
   
   获取最新tags，找个顺眼的服务器部署（不要部署在国内服务商）
   
   node (path)/server.js
   
   需要端口3000  

3. 客户端：
   
   获取最新的tags，开箱即用
   
   使用时运行 python ./cli.py  


## 贡献  

欢迎贡献！请遵循以下步骤：  

Fork 仓库  

创建新分支（git checkout -b feature/your-feature）  

提交修改（git commit -am 'Add new feature'）  

推送到分支（git push origin feature/your-feature）  

创建一个新的 Pull Request  

## 许可证  

本项目使用 MIT 许可证。  

## 致谢  

NodeJS  

Python  

FireFoxPortable  

FireFox
