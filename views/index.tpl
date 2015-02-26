<html>
<head>
    <title>OCR DEMO</title>
    <link rel="stylesheet" type="text/css" href="static/style.css">
</head>
<body>
    <div class="main">
        <div>This is the pure OCR without any pre processing on the image. Picture should be of high resolution and also there should not be a lot of illunimation artifacts and shades on the image.</div>
        <br>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            Select a file: <input type="file" name="upload" />
            <input type="submit" value="Start upload" class="button"/>
        </form>
    </div>
</body>
</html>