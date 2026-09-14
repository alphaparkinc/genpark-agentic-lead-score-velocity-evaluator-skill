import json, sys
from client import AgenticLeadScoreVelocityEvaluatorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "lead-score-velocity", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "evaluate_lead_score", "description": "Scores customer engagement velocity and outputs next best marketing action."}]}}
    elif method == "tools/call":
        client = AgenticLeadScoreVelocityEvaluatorClient()
        res = client.evaluate_lead_score()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AgenticLeadScoreVelocityEvaluatorClient()
        print(json.dumps(client.evaluate_lead_score(), indent=2))
