#!/bin/bash

# Test get endpoint
curl --request GET http://localhost:5000/api/timeline_post

# Test post endpoint
curl --request POST http://localhost:5000/api/timeline_post -d 'name=fiona&email=laygo.fiona@gmail.com&content=testing via bash script'

# Test delete
curl --request DELETE http://localhost:5000/api/timeline_post
