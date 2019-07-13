package com.oops;

class Fruit {

    public Fruit() {

        System.out.println("Constructor called");

        System.out.println("Super class object hashcode :" +
                this.hashCode());

        System.out.println(this.getClass().getName());

    }

}

class Apple extends Fruit {

    public Apple() {

        System.out.println("Sub class object hashcode :" +
                this.hashCode());

        System.out.println(this.getClass().getName());

        System.out.println("Sub Constructor called");

    }

}

class A {

    static int y = 0;
    int x = 10;

}

class Test {

    public static void main(String[] args) {

        System.out.println(A.y);

        A a1 = new A();

        A a2 = new A();

        a1.x = 20;

        a2.x = 50;

        System.out.println(A.y);

        A.y++;

        System.out.println(a1.x);

        System.out.println(A.y);

        A.y++;

        System.out.println(a2.x);

        System.out.println(A.y);

    }

}