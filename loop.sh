API_KEY="x"
SECRET_KEY="x"

# Set up the request:
BASE_URL="https://api.binance.com"
API_METHOD="POST"
API_CALL="api/v3/order"
SYMBOL="PYTHUSDT"
SIDE="BUY"
TYPE="MARKET"
QUANTITY="10"

PARM="symbol=$SYMBOL&side=$SIDE&type=$TYPE&quantity=$QUANTITY"
BOOL=true

while $BOOL
do
  timestamp=$(date +%s000)
  API_PARAMS="$PARM&timestamp=$timestamp"
  signature=$(echo -n "$API_PARAMS" | openssl dgst -sha256 -hmac "$SECRET_KEY" | awk '{print $2}')
  
  # Send the request:
  response=$(curl -X "$API_METHOD" -H "X-MBX-APIKEY: $API_KEY" \
  "$BASE_URL/$API_CALL?$API_PARAMS&signature=$signature")
  
  status=$(echo "$response" | jq -r '.status')
  # Check if the status is "FILLED"
  if [ "$status" = "FILLED" ]; then
      echo "Order Filled:"
      BOOL=false
  else
      echo "Order not filled"
  fi
done
