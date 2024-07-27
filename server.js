const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

const NORMAL_PASSWORD = 'normalpassword';
const SPECIAL_PASSWORD = 'specialpassword';

let loginAttempts = 0;

// 设置存储引擎
const storage = multer.diskStorage({
  destination: './uploads/',
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
});

// 初始化上传
const upload = multer({
  storage: storage
}).single('file');

// 创建上传目录（如果不存在）
const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)){
    fs.mkdirSync(uploadDir);
}

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// 中间件：鉴权
app.use((req, res, next) => {
  const password = req.headers['password'];
  if (!password) {
    return res.status(401).json({ message: 'Password required' });
  }

  if (password === NORMAL_PASSWORD) {
    loginAttempts = 0;  // 重置错误次数
    next();
  } else {
    loginAttempts += 1;
    if (password === SPECIAL_PASSWORD || loginAttempts >= 3) {
      return res.status(403).json({ message: 'Special action triggered' });
    } else {
      return res.status(401).json({ message: 'Authentication failed' });
    }
  }
});

// 处理文件上传
app.post('/upload', (req, res) => {
  upload(req, res, (err) => {
    if (err) {
      return res.status(500).json({ message: 'File upload failed', error: err.message });
    }
    res.status(200).json({ message: 'File uploaded successfully' });
  });
});

// 处理文件下载
app.get('/download/:filename', (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join(__dirname, 'uploads', filename);
  res.download(filePath, (err) => {
    if (err) {
      res.status(500).json({ message: 'File download failed', error: err.message });
    }
  });
});

// 启动服务器
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
