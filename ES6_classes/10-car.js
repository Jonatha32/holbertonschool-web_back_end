export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  get color() {
    return this._color;
  }

  get motor() {
    return this._color;
  }

  cloneCar() {
    const SymKey = Symbol('Car');
    const clone = Object.assign(
      Object.create(Object.getPrototypeOf(this)),
      { [SymKey]: true }
    );
    return clone;
  }
}
