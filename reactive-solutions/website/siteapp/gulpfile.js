const gulp = require('gulp');
const minify = require('gulp-minify');
const uglifycss = require('gulp-uglifycss');


gulp.task('compress-js', function() {
  gulp.src(['static/source-js/*.js', 'static/mjs/*.mjs'])
    .pipe(minify())
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


gulp.task('default', ['compress-js', 'compress-css', 'watch-js', 'watch-css']);
