const gulp = require('gulp');
const uglifycss = require('gulp-uglifycss');
const uglify = require('gulp-uglify');


gulp.task('compress-js', function() {
  gulp.src(['static/source-js/*.js'])
    .pipe(uglify())
    .pipe(gulp.dest('static/js'))
});


gulp.task('compress-css', function () {
  gulp.src('static/source-css/*.css')
    .pipe(uglifycss({
      "maxLineLen": 80,
      "uglyComments": true
    }))
    .pipe(gulp.dest('static/css'));
});


gulp.task('watch-js', function() {
    gulp.watch('static/source-js/*.js', ['compress-js']);
});


gulp.task('watch-css', function() {
    gulp.watch('static/source-css/*.css', ['compress-css']);
});


gulp.task('default', ['compress-css', 'compress-js', 'watch-css', 'watch-js']);
