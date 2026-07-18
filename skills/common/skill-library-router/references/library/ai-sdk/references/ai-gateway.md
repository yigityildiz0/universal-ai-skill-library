---
title: Vercel AI Gateway
description: Reference for using Vercel AI Gateway with the AI SDK.
---

# Vercel AI Gateway

Vercel AI Gateway is one optional AI SDK provider layer. Use it only when the project or user has chosen its routing, authentication, pricing, privacy, and regional tradeoffs. The AI SDK also supports direct provider packages and custom/provider-registry configurations.

## Authentication

Authenticate with OIDC (for Vercel deployments) or an [AI Gateway API key](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway%2Fapi-keys&title=AI+Gateway+API+Keys):

```env filename=".env.local"
AI_GATEWAY_API_KEY=your_api_key_here
```

## Usage

In releases where the gateway is the configured global provider, a namespaced string can resolve through it. Verify the installed AI SDK version and project bootstrap before relying on this behavior:

```ts
import { generateText } from 'ai';

const { text } = await generateText({
  model: 'provider/verified-model-id',
  prompt: 'What is love?',
});
```

You can also explicitly import and use the gateway provider:

```ts
// Option 1: Import from 'ai' package (included by default)
import { gateway } from 'ai';
model: gateway('provider/verified-model-id');

// Option 2: Install and import from '@ai-sdk/gateway' package
import { gateway } from '@ai-sdk/gateway';
model: gateway('provider/verified-model-id');
```

## Find Available Models

**Important**: Verify the intended model ID from current gateway metadata before writing code. Never use model IDs from memory, and do not enumerate the catalog unless model selection is actually part of the task.

List all available models through the gateway API:

```bash
curl https://ai-gateway.vercel.sh/v1/models
```

Filter by provider when comparison is required:

```bash
# Anthropic models
curl -s https://ai-gateway.vercel.sh/v1/models | jq -r '.data[] | select(.id | startswith("anthropic/")) | .id'

# OpenAI models
curl -s https://ai-gateway.vercel.sh/v1/models | jq -r '.data[] | select(.id | startswith("openai/")) | .id'

# Google models
curl -s https://ai-gateway.vercel.sh/v1/models | jq -r '.data[] | select(.id | startswith("google/")) | .id'
```

Choose a model from current gateway metadata according to the user's quality, latency, cost, region, and capability requirements. Do not select by version-like sorting alone.
