# GLM-4.6-FP8 OpenAI-Compatible API

VERIFIED OpenAI-compatible API client for GLM-4.6-FP8 via Zai Inference Provider.

## Quick Start

### Prerequisites
- HuggingFace API token with access to GLM-4.6-FP8 model
- Set environment variable: `HF_TOKEN`

### API Configuration

**Base URL:** `https://router.huggingface.co/v1`
**Model ID:** `zai-org/GLM-4.6-FP8:zai-org`
**Provider:** Zai (verified working)

## Installation

### Python
```bash
pip install openai
```

### JavaScript/Node.js
```bash
npm install openai
```

## Usage Examples

### Python (OpenAI SDK)

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="zai-org/GLM-4.6-FP8:zai-org",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)
```

### JavaScript (OpenAI SDK)

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    baseURL: "https://router.huggingface.co/v1",
    apiKey: process.env.HF_TOKEN,
});

const chatCompletion = await client.chat.completions.create({
    model: "zai-org/GLM-4.6-FP8:zai-org",
    messages: [
        {
            role: "user",
            content: "What is the capital of France?",
        },
    ],
});

console.log(chatCompletion.choices[0].message);
```

### cURL

```bash
curl https://router.huggingface.co/v1/chat/completions \
  -H "Authorization: Bearer $HF_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "zai-org/GLM-4.6-FP8:zai-org",
    "messages": [
      {
        "role": "user",
        "content": "What is the capital of France?"
      }
    ]
  }'
```

## API Details

### Model Information
- **Model Size:** 358B parameters
- **Quantization:** FP8 (efficient inference)
- **Context Window:** 200K tokens (expanded from 128K)
- **License:** MIT

### Supported Languages
- English
- Chinese
- Multi-lingual support

### Performance Features
- Superior coding performance
- Better real-world application performance
- Improved agentic capabilities

## Implementation Status

✅ **VERIFIED WORKING**
- Tested with Zai Inference Provider
- OpenAI-compatible API confirmed functional
- Multiple language examples provided

## References

- [Model Card](https://huggingface.co/zai-org/GLM-4.6-FP8)
- [Zai Documentation](https://docs.z.ai/guides/overview/quick-start)
- [Technical Report](https://arxiv.org/abs/2508.06471)

## Support

For issues or questions about the API, visit:
- Model page: https://huggingface.co/zai-org/GLM-4.6-FP8
- Z.ai documentation: https://docs.z.ai/
