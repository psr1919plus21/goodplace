gulp = require("gulp")
coffee = require("gulp-coffee")
watch = require("gulp-watch")
sass = require("gulp-sass")
autoprefixer = require("gulp-autoprefixer")

path =
	src:
		coffee: "./src/coffee/*.coffee"
		js: "./src/js/*.js"
		css: "./src/css/*.css"
		sass: "./src/sass/*.scss"
		html: ['./src/html/**/*.html','!./src/html/templates/**/*.html']
		fonts: "./src/fonts/*"
		img: "./src/img/*"
		imgSvg: "./src/img/*.svg"
		imgJpg: "./src/img/*.jpg"
		imgPng: "./src/img/*.png"
	dist:
		js: "./dist/js/"
		css: "./dist/css/"
		fonts: "./dist/fonts/"
		img: "./dist/img/"

gulp.task "fonts", ->
	gulp.src(path.src.fonts)
	.pipe gulp.dest path.dist.fonts

gulp.task "imagemin", ->
	gulp.src(path.src.img)
	.pipe gulp.dest path.dist.img

gulp.task "js", ->
	gulp.src(path.src.js)
	.pipe gulp.dest path.dist.js

gulp.task "css", ->
	gulp.src(path.src.css)
	.pipe gulp.dest path.dist.css
	
# gulp.task "imageminJpg", ->
# 	gulp.src(path.src.imgJpg)
# 	# .pipe imagemin
# 	# 	progressive: true
# 	.pipe gulp.dest path.dist.img

# gulp.task "imageminPng", ->
# 	gulp.src(path.src.imgPng)
# 	# .pipe imagemin
# 	# 	use: [pngquant()]
# 	.pipe gulp.dest path.dist.img

# gulp.task "imageminSvg", ->
# 	gulp.src(path.src.imgSvg)
# 	# .pipe svgmin()
# 	.pipe gulp.dest path.dist.img

# gulp.task "teddy", ->
# 	gulp.src(path.src.html)
# 	.pipe(teddy.compile())
# 	.pipe gulp.dest "./"

# gulp.task "htmluncompress", ["teddy"], ->
# 	gulp.src("./*.html")
# 	.pipe prettify({indent_size: 2})
# 	.pipe gulp.dest("./")

gulp.task "coffee", ->
	gulp.src(path.src.coffee)
	.pipe(do coffee)
	.pipe gulp.dest path.dist.js

gulp.task "sass", ->
	gulp.src(path.src.sass)
	.pipe(do sass)
	.pipe gulp.dest path.dist.css

gulp.task "autoprefixer", ["sass"], ->
	gulp.src("./dist/css/*.css")
	.pipe(do autoprefixer)
	.pipe gulp.dest path.dist.css

gulp.task "watch", ->
	watch path.src.coffee, ->
		gulp.run "coffee"
	watch path.src.sass, ->
		gulp.run "autoprefixer"
	
	
gulp.task "dev", ["css", "fonts", "imagemin", "coffee", "js", "autoprefixer", "watch"], ->

gulp.task "default", ["css", "fonts", "imagemin", "coffee", "js", "autoprefixer"], ->
