# 용어 및 개념정리 5.

## 1. 리터럴 표기법과 빌트인 생성자 함수
- 엄밀히 말하면 리터럴 표기법에 의해 생성된 객체는 생성자 함수에 의해 생성된 객체는 아님.

- 리터럴 표기법에 의해 생성된 객체와 생성자 함수에 의해 생성된 객체는 미묘한 차이가 있지만 프로토타입의 constructor 프로퍼티를 통해 확인해 보면 생성자 함수와 연결되어 있기 때문에 본질적인 면에서 큰 차이는 없음.

- 빌트인 생성자 함수는 전역 객체가 생성되는 시점에 생성되고, 생성된 프로토타입은 prototype 프로퍼티에 바인딩됨.

- 객체의 경우, 객체 리터럴에 의해 생성된 객체와 Object 생성자 함수를 호출하여 생성된 객체는 추상 연산(OrdinaryObjectCreate)를 호출하여 빈 객체를 생성하는 점에서는 동일, new.target의 확인이나 프로퍼티를 추가하는 처리 등에서는 다름.

- 함수 객체의 경우, Function 생성자 함수를 호출하여 생성된 함수 객체는 렉시컬 스코프를 만들지 않고 전역 함수인 것처럼 스코프를 생성하며 클로저를 만들지 않는 면에서 미묘한 차이가 있음.

- 생성자 함수 종류 : String, Number, Boolean, Function, Array, Date, RegExp, Promise 등

- 표로 정리

리터럴 표기법 | 생성자 함수(빌트인) | 프로토타입
:---: | :---: | :---:
객체 리터럴 | Object | Object.prototype
함수 리터럴 | Function | Function.prototype
배열 리터럴 | Array | Array.prototype
정규 표현식 리터럴 | RegExp | RegExp.prototype
---

## 2. 객체 생성 방식
공통점 : 추상 연산(OrdinaryObjectCreate)에 의해 생성.   
프로토타입은 추상 연산에 전달되는 인수에 의해 결정되고, 인수는 객체가 생성되는 시점에 객체 생성 방식에 의해 결정됨.   
생성자 함수와 프로토타입은 언제나 쌍으로 존재함.

생성 방식 | 프로토타입
:---: | :---: 
객체 리터럴 | Object.prototype
Object 생성자 함수 | Object.prototype
사용자 정의 생성자 함수 | 생성자 함수 이름.prototype<br>constructor 프로퍼티만 가짐<br>상위 객체로 Object.prototype 가짐 
Object.create 메서드
클래스(ES6)
---

## 3. 객체 생성 방식 차이 정리 (객체 리터럴[ ] vs. Object 생성자 함수 vs. 사용자 정의 생성자 함수)
- 객체 리터럴 { };
  - <u>단 하나</u>의 객체만 생성함. 프로퍼티 구조가 동일한 객체를 여러 개 생성해야 하는 경우, 매번 같은 프로퍼티를 기술해야 하기 때문에 비효율적임.

- Object 생성자 함수 
  - 빈 객체를 생성하기 때문에 객체 리터럴을 통해 객체를 생성하는 것이 더 간편함.
  ```javascript
  // new 연산자와 Object 생성자 함수를 호출하면 빈 객체 생성
  const person = new Object();

  // 프로퍼티 추가하여 객체 완성
  person.name = 'Oh';
  person.sayHi = function () {
      console.log('Hi! ' + this.name);
  };
  ```

- 사용자 정의 생성자 함수
  - 함수 선언문으로 function 정의하고, new 연산자와 함께 함수 이름을(내부적으로 함수 이름과 동일한 이름으로 식별자 생성) 호출하여 객체(인스턴스)를 생성하는 함수.
  - 생성자 함수에 의해 생성된 객체를 인스턴스라고 함.
  - 프로퍼티 구조가 동일한 객체를 <u>여러 개</u> 생성할 수 있음. 
  - 생성자 함수의 prototype 프로퍼티에 의해 바인딩된 프로토타입은 constructor만 가짐.
  - 프로토타입은 constructor(생성자 함수로서 호출할 수 있는)이 평가되어 함수 객체를 생성하는 시점에 더불어 생성됨.
  - 모든 객체는 프로토타입을 가지기 때문에 생성된 프로토타입의 프로토타입은 Object.prototype. 
- 표로 정리

객체 생성 방식 | 엔진의 객체 생성 | 인스턴스의 prototype 객체
:---: | :---: | :---:
객체 리터럴 | Object() 생성자 함수라고 치자<br>미묘한 차이 존재 | Object.prototype
Object() 생성자 함수 | Object() 생성자 함수 | Object.prototype
생성자 함수 | 생성자 함수 | 생성자 함수 이름.prototype
---

## 4. prototype 프로퍼티 vs. [[prototype]] 
prototype 프로퍼티와 __proto__접근자 프로퍼티는 동일한 프로토타입을 가리키지만 프로퍼티를 사용하는 주체가 다름.
- prototype 프로퍼티
  - 함수 객체만 가지고 있는 프로퍼티(일반객체x).
  - 여러 개의 객체를 생성하는 사용자 정의 생성자 함수일 때 의미가 있음.
  - 일반 함수(함수 선언문, 함수 표현식)도 소유하고 있지만, 객체를 생성하지 않기 때문에 의미가 없음.
  - prototype 프로퍼티에 의해 생성자 함수와 프로토타입이 바인딩됨.

- [[prototype]]
  - 함수를 포함한 모든 객체가 가지고 있는(엄밀히 말하면 Object.prototype으로부터 상속받은) 인터널 슬롯(내부 슬롯). 
  - 내부 슬롯에 직접 접근 불가능, __proto__접근자 프로퍼티를 통해 간접 접근 가능.
  - [[prototype]]의 값은 null 또는 객체.
  - 상속을 구현하기 위해 사용.

- 표로 정리

구분 | 소유 | 값 | 사용 주체 | 사용 목적
:---: | :---: | :---: | :---: | :---:
prototype 프로퍼티 | constructor | 프로토타입의 참조 | 사용자 정의 생성자 함수 | 생성자 함수 자신이 생성할 객체(인스턴스)의 프로토타입을 할당하기 위해 사용 
__proto__접근자 프로퍼티 | 모든 객체 | 프로토타입의 참조 | 모든 객체 | 객체가 자신의 프로토타입에 접근 또는 교체하기 위해 사용.


<br>

## # Reference
1. https://poiemaweb.com/js-prototype



