# django_airbnb_clone

1. pipenv --three
2. pipenv shell
3. pipenv install Django
4. python manager.py migrate
5. application 설치
   - django-admin startapp rooms
   - django-admin startapp users
   - django-admin startapp reviews
   - django-admin startapp conversations
   - django-admin startapp lists
   - django-admin startapp reservations

- 나라리스트 : https://github.com/SmileyChris/django-countries
- seed : https://github.com/Brobin/django-seed

UI
 - tailwindcss.com
 - builtwithtailwind.com

 Setting up TailwindCSS with Gulp
 1. npm init
 2. glupjs.com
 3. npm install gulp gulp-postcss gulp-sass gulp-csso node-sass -D
 4. npm install tailwindcss -D
 5. npx tailwind init   --> tailwind.config.js생성됨
 6. gulpfile.js 만들기
 --------------------------------------------------------
   const gulp = require('gulp')
   const css = () => {
    const postCSS = require('gulp-postcss');
    const sass = require('gulp-sass');
    const minify = require('gulp-csso');
    sass.compiler = require('node-sass');
    return gulp
        .src('assets/scss/styles.css')
        .pipe(sass().on('error', sass.logError))
        .pipe(postCSS([
            require('tailwindcss'),
            require('autoprefixer')
        ]))
        .pipe(minify())
        .pipe(gulp.dest('static/css'));
   };
   exports.default = css
 --------------------------------------------------------
 7. assets 폴더생성 
 8. npm i autoprefixer -D
 9. package.json에 scrpt 추가
      "scripts": {
         "css":"gulp"
      },
 10. assets/scss/styles.scss 생성
      @tailwind base;
      @tailwind components;
      @tailwind utilities;
 11. 실행: npm run css  --> static/css/styles.css 파일 생성됨