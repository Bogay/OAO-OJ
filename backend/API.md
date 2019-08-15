# [API reference](https://hackmd.io/@AlaRduTP/OAO-OJ-API)

1. [Admin](#admin)
2. [Judge](#judge)
3. [Problems](#problems)

## Common specifications

### Status codes

-  
  The following status codes are returned by the this API.

  | Status code | Description |
  | --- | --- |
  | 200 OK | Request successful |
  | 400 Bad Request | Problem with the request |
  | 404 Not Found | Something not found in the database |
  | 500 Internal Server Error | Error on the internal server |

### Error responses

- The following JSON data is returned in the response body when an error occurs.

  | Property | Type | Description |
  | --- | --- | --- |
  | err | String | Message containing information about the error. |

## Admin

### Get problems list

- 
  Get problems list that admin can manage.

#### HTTP request

- 
  `GET /admin/probs`

#### Response

- 
  Returns the status code `200` and an **array** of JSON objects with following information.

  | Property | Type | Description |
  | --- | --- | --- |
  | pid | String | Problem ID |
  | title | String | Title of problem |
  | status | Number | Status of problem<br><ul><li>- `0` Online</li><li>- `1` Offline</li><li>- `2` Hidden</li></ul> |

#### Example response

- 
  ```json
  [
      {
          "pid": "0000",
          "title": "Hello, OAO-OJ",
          "status": 0
      },
      {
          "pid": "0001",
          "title": "ABC",
          "status": 1
      }
  ]
  ```

## Judge

### Submit the script

- 
  Submit the script and judge it.

#### HTTP request

- 
  `POST /judge/submit`

#### Request body

- 
  | Property | Type | Required | Description |
  | --- | --- | --- | --- |
  | pid | String | Required | Problem ID |
  | script | String | Required | Script to judge |
  | input-data | String | Optional | User-defined input data |
  | output-data | String | Optional | User-defined output data |

#### Response

- 
  Returns the status code `200` and JSON object with following information.

  | Property | Type | Description |
  | --- | --- | --- |
  | taskCount | Number | Number of testdatas |
  | scriptLen | Number | Len of the script |
  | results | Array of strings | Judge results <br><ul><li>- `AC` Accepted</li><li>- `WA` Wrong answer</li><li>- `LLE` Line limit exceeded</li></ul> |

#### Example response

- 
  ```json
  {
      "scriptLen": 83,
      "taskCount": 2,
      "result": [
          "AC",
          "WA"
      ]
  }
  ```

## Problems

### Get problems list

- 
  Get problems list that all users can see it.

#### HTTP request

- 
  `GET /probs`

#### Response

- 
  Returns the status code `200` and an **array** of JSON objects with following information.

  | Property | Type | Description |
  | --- | --- | --- |
  | pid | String | Problem ID |
  | title | String | Title of problem |
  | status | Number | Status of problem <br><ul><li>- `0` Todo</li><li>- `1` Solved</li><li>- `2` Tried but in vain</li></ul> |
  | submissionsAcRate | Number | Submissions AC rate of problem |
  | usersAcRate | Number | Users AC rate of problem |

#### Example response

- 
  ```json
  [
      {
          "pid": "0000",
          "title": "Hello, OAO-OJ",
          "status": 0,
          "submissionsAcRate": 0,
          "usersAcRate": 0
      },
      {
          "pid": "0001",
          "title": "ABC",
          "status": 1,
          "submissionsAcRate": 0,
          "usersAcRate": 0
      }
  ]
  ```

---

### Get details of a problem

- 
  Get details of a problem that are displayed to all users.

#### HTTP request

- 
  `GET /probs/{pid}`

  #### Path parameters
  
  -
    | Parameter | Description |
    | --- | --- |
    | pid | Problem ID |

#### Response

- 
  Returns the status code `200` and JSON objects with following information.

  | Property | Type | Description |
  | --- | --- | --- |
  | pid | String | Problem ID |
  | title | String | Title of problem |
  | desc | String | Description of problem in Markdown |

#### Example response

- 
  ```json
  {
      "pid": "0000",
      "title": "Hello, OAO-OJ",
      "desc": "# Hello, OAO-OJ\n\n## Problem Description\n\nsay hello to OAO-OJ!\n\n## Input Format\n\nno input in this problem\n\n## Output Format\n\nprint `hello, OAO-OJ` in one line\n"
  }
  ```

---

### Add a new problem

- 
  Add a new problem to database.

#### HTTP request

- 
  `POST /probs/{pid}`

  #### Path parameters
  
  - 
    | Parameter | Description |
    | --- | --- |
    | pid | New problem ID |

#### Request body

- 
  | Property | Type | Required | Description |
  | --- | --- | --- | --- |
  | title | String | Required | Title of new problem |
  | desc | String | Required | Description of new problem in Markdown |
  | info | JSON string | Required | *Information of new problem* |
  | testdatas | JSON string | Required | *Testdatas of new problem* |

  #### Information of new problem
  
  - 
    | Property | Type | Required | Description |
    | --- | --- | --- | --- |
    | testdatas | Array of arrays | Required | Array of *information arrays of testdata* |

    #### Information array of testdata
    
    - 
      | Index | Type | Description |
      | --- | --- | --- |
      | 0 | String | Testdata name |
      | 1 | Number | Time limit |
      | 2 | Number | Memory limit |

  #### Testdata of new problem
  
  - 
    | Property | Type | Required | Description |
    | --- | --- | --- | --- |
    | *{name}* | Array of strings | Required | *User-defined data array* for each testdata |

    #### Property parameters
    
    - 
      | Parameter | Description |
      | --- | --- |
      | name | Testdata name |

    #### User-defined data array
    
    - 
      | Index | Type | Description |
      | --- | --- | --- |
      | 0 | String | Input data |
      | 1 | String | Output data |

#### Example request body

- 
  ```json
  {
      "title": "ABC",
      "desc": "# MarkDown",
      "info": "{ 'testdatas': [ ['01', 3, 512], ['02', 3, 512] ] }",
      "testdatas": "{ '01': [ '01-in', '01-out' ], '02': [ '02-in', '02-out' ] }"
  }
  ```

#### Response

- 
  Returns the status code `200` and JSON objects with following information.

  | Property | Type | Description |
  | --- | --- | --- |
  | msg | String | Success message |

#### Example response

- 
  ```json
  {
      "msg": "Ok."
  }
  ```

---

### Delete a problem

- 
  Remove a problem from database.

#### HTTP request

- 
  `DELETE /probs/{pid}`

  #### Path parameters
  
  - 
    | Parameter | Description |
    | --- | --- |
    | pid | Problem ID |

#### Response

- 
  Returns the status code `200` and JSON objects with following information.

  | Property | Type | Description |
  | --- | --- | --- |
  | msg | String | Success message |

#### Example response

- 
  ```json
  {
      "msg": "Ok."
  }
  ```
