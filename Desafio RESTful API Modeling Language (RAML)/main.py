
doc = doc = '''
#%RAML 1.0
title: desafio-12
version: v1
mediaType: application/json

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string

  Agent:
    type: object
    discriminator: agent
    properties:
      agent_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
      status:
        type: boolean
        required: true
        example: true
      environment:
        type: string
        required: true
        example: "environment example"
      version:
        type: string
        required: true
        example: "versi"
      address:
        type: string
        required: true
        example: "address example"
      user_id:
        type: integer
        required: true
        example: 1
    example:
      agent_id: 1
      user_id: 1
      name: "name example"
      status: true
      environment: "environment example"
      version: "versi"
      address: "address example"

  Event:
    type: object
    discriminator: event
    properties:
      event_id:
        type: integer
        required: true
        example: 1
      agent_id:
        type: integer
        required: true
        example: 1
      level:
        type: string
        required: true
        example: "level example"
      payload:
        type: string
        required: true
        example: "payload example"
      shelved:
        type: boolean
        required: true
        example: true
      date:
        type: datetime
        required: true
        example: "2018-11-26T16:17:18Z"
    example:
      event_id: 1
      agent_id: 1
      level: "level example"
      data: "payload example"
      shelve: true

  Group:
    type: object
    discriminator: group
    properties:
      group_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
    example:
      group_id: 1
      name: "group example"

  User:
    type: object
    discriminator: user
    properties:
      user_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
      email:
        type: string
        required: true
        example: "email@example.com"
      last_login:
        type: date-only
        required: true
        example: "2019-11-20"
      group_id: 
        type: string
        required: true
        example: 1

  Response:
    discriminator: response
    properties:
      message:
        type: string
        example: "message example"

securitySchemes:
  JWT:
    description: Autenticação JWT
    type: x-{other}
    describedBy:
      headers:
        Authorization:
          description: X-AuthToken
          type: string
          required: true
      responses:
        201:
          body: 
            application/json:
              description: Token generated
        400:
          body: 
            application/json:
              description: Expired Token
    settings:
      roles: []

/auth/token:
    post:
      description: Return JWT
      body:
        application/json:
          type: Auth
          username: string
          password: string
      responses: 
        201:
          body: 
            application/json:
              description: Token generated
        400:
          body: 
            application/json:
              description: Expired Token
      securedBy: [JWT]

/agents:
  get:
    description: Return list agents
    responses: 
      200:
        body:
          type: Response
          example:
            message: Listed
      401:
        body:
          type: Response
          example:
            message: Unauthorized
      404:
        body:
          type: Response
          example:
            message: Not Found
    securedBy: [JWT]
  post:
    description: New Agent
    body: 
      application/json:
        example: {
            "agent_id": 1,
            "user_id": 1,
            "name": "name example",
            "status": true,
            "environment": "environment example",
            "version": "versi",
            "address": "address example"
          }
    responses: 
      201:
        body:
          type: Response
          example:
            message: Created
      401:
        body:
          type: Response
          example:
            message: Unauthorized
    securedBy: [JWT]

  /{id}:
    get:
      description: Agent detail
      responses: 
        200:
          body:
            type: Response
            example:
              message: Created
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    put:
      responses:
        200:
          body:
            type: Response
            example:
              message: Created
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    delete:
      description: Delete Agent
      responses:
        200:
          body:
            type: Response
            example:
              message: Deleted
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]

  /{id}/events:
    get:
      description: Events list
      responses:
        200:
          body:
            type: Event[]
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    post:
      body: 
        application/json:
          example: {
              "event_id": 1,
              "agent_id": 1,
              "level": "level example",
              "data": "payload example",
              "shelve": true
            }
        201:
          body:
            type: Response
            example:
              message: Created
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    put:
      description: Update Event
      body:
        type: Event
        200:
          body:
            type: Response
            example:
              message: Updated
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      responses:
        200:
          body:
            type: Event
        400:
          body:
            type: Response
            example:
              message: Bad request
      securedBy: [JWT]
    delete:
      description: Delete Event
      body: 
        application/json:
          properties: 
            example: {
              }
        200:
          body:
            type: Response
            example:
              message: Deleted
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      responses:
        200:
          body:
            type: Response
            example:
              message: Deleted
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]

/groups:
  get:
    description: Group list
    responses:
      200:
        body:
          type: Group[]
      401:
        body:
          type: Response
          example:
            message: Not found
    securedBy: [JWT]
  post:
    description: Create Group
    body:
      application/json:
        properties: 
          example: {
              "group_id": 1,
              "name": "group"
            }
        example: {
              "group_id": 1,
              "name": "group"
            }
    responses:
      201:
        body:
          type: Group
      401:
        body:
          type: Response
          example:
            message: Unauthorized
    securedBy: [JWT]

  /{id}:
    get:
      description: Group detail
      responses:
        200:
          body:
            type: Group[]
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    put:
      description: Edit Group
      body:
        type: Group
      responses:
        200:
          body:
            type: Group
        401:
          body:
            type: Response
            example:
              message: Unauthorized
      securedBy: [JWT]
    delete:
      description: Delete Group
      responses:
        204:
          body:
            type: Response
            example:
              message: Deleted
        400:
          body:
            type: Response
            example:
              message: Bad request
      securedBy: [JWT]

/users:
  get:
    description: User list
    responses:
      200:
        body:
          type: User[]
    securedBy: [JWT]
  post:
    description: Create User
    body:
      application/json:
        properties:
          example: {
              "user_id": 1,
              "name": "name",
              "email": "email",
              "last_login": "2019-11-20",
              "group_id": 1
            }
    responses:
      201:
        body:
          type: User
      401:
        body:
          type: Response
          example:
            message: Unauthorized
      404:
        body:
          type: Response
          example:
            message: Not Found
    securedBy: [JWT]

  /{id}:
    get:
      description: User detail
      responses:
        200:
          body:
            type: User[]
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    put:
      description: Edit User
      body:
        type: User
      responses:
        200:
          body:
            type: User
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    delete:
      responses:
        200:
          body:
            type: Response
            example:
              message: Deleted
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
'''