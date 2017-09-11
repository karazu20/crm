'use strict'

const gulp = require('gulp')
const stylus = require('gulp-stylus')

gulp.task('dev:css', function () {
  gulp
  .src('assets/styles/*.styl')
  .pipe(stylus())
  .pipe(gulp.dest('static/css'))
})

gulp.task('watch', function () {
  gulp.watch('assets/styles/**/*.styl', ['dev:css'])
})

gulp.task('default', ['dev:css', 'watch'])

