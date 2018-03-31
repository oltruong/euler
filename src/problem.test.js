const problem1 = require('./problem1');
const problem2 = require('./problem2');
const problem3 = require('./problem3');
const problem4 = require('./problem4');
const problem5 = require('./problem5');
const problem6 = require('./problem6');
const problem7 = require('./problem7');

test('problem1', () => {
    expect(problem1()).toBe(233168);
});

test('problem2', () => {
    expect(problem2()).toBe(4613732);
});

test('problem3', () => {
    expect(problem3()).toBe(6857);
});

test('problem4', () => {
    expect(problem4()).toBe(906609);
});

test('problem5', () => {
    expect(problem5()).toBe(232792560);
});

test('problem6', () => {
    expect(problem6()).toBe(25164150);
});

test('problem7', () => {
    expect(problem7()).toBe(104743);
});
