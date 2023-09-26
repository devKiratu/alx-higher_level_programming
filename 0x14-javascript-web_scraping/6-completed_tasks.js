#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, data) => {
  if (error) {
    throw error;
  } else {
    const output = {};
    const todos = JSON.parse(data);
    const userIds = new Set(todos.map(todo => todo.userId));
    userIds.forEach(id => {
      const completeTodos = todos.reduce((count, todo) => {
        if (todo.userId === id && todo.completed) {
          count += 1;
        }
        return count;
      }, 0);
      if (completeTodos > 0) {
        output[id] = completeTodos;
      }
    });
    console.log(output);
  }
});
