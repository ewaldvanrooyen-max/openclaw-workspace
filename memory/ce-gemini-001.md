# CE-GEMINI-001: Gemini API Integration for ContentEngin

## Overview
Integration of Google Gemini API for dynamic script generation in ContentEngin workflows.

## Prerequisites
- Google AI Studio API key: https://aistudio.google.com/app/apikey
- Node.js environment

## Implementation

### 1. Installation
```bash
npm install @google/generative-ai
```

### 2. Gemini API Client (`lib/gemini.js`)
```javascript
const { GoogleGenerativeAI } = require('@google/generative-ai');

// Initialize with API key (from env: GEMINI_API_KEY)
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

const model = genAI.getGenerativeModel({
  model: 'gemini-2.0-flash',
  generationConfig: {
    temperature: 0.9,
    maxOutputTokens: 2048,
  }
});

/**
 * Generate a script based on workflow type and inputs
 * @param {string} workflowType - 'demo', 'narrator', 'teacher', 'closer'
 * @param {Object} inputs - { topic, audience, duration, tone, etc }
 * @returns {Promise<string>} Generated script
 */
async function generateScript(workflowType, inputs) {
  const prompts = {
    demo: `Create a ${inputs.duration || '5-minute'} demo script for ${inputs.product}. 
           Target audience: ${inputs.audience}. Tone: ${inputs.tone || 'professional'}.
           Include: Hook, Problem, Solution, Features, CTA.``,
    
    narrator: `Write a narration script for a ${inputs.type} video about ${inputs.topic}.
               Duration: ${inputs.duration || '2 minutes'}. 
               Style: ${inputs.style || 'engaging and informative'}.`,
    
    teacher: `Create an educational script teaching ${inputs.topic}.
              For: ${inputs.audience || 'beginners'}.
              Length: ${inputs.lessons || '3'} lessons.
              Include learning objectives and summary.`,
    
    closer: `Write a persuasive closing script for ${inputs.offer}.
             Target: ${inputs.audience}.
             Urgency: ${inputs.urgency || 'medium'}.
             Include: Value recap, Bonus, Deadline, Guarantee.`
  };
  
  const prompt = prompts[workflowType] || prompts.demo;
  
  try {
    const result = await model.generateContent(prompt);
    return result.response.text();
  } catch (error) {
    console.error('Gemini API Error:', error);
    throw error;
  }
}

module.exports = { generateScript };
```

### 3. Environment Configuration
```bash
# Add to .env
GEMINI_API_KEY=your_api_key_here
```

### 4. Workflow Integration Example
```javascript
// In your workflow handler
const { generateScript } = require('./lib/gemini');

async function runDemoWorkflow(inputs) {
  const script = await generateScript('demo', {
    product: inputs.productName,
    audience: inputs.targetMarket,
    duration: inputs.length,
    tone: inputs.tone
  });
  
  return { script, status: 'generated' };
}
```

## API Key Setup
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Create new API key
4. Copy to `GEMINI_API_KEY` env var

## Pricing (Reference)
- Gemini 2.0 Flash: Free tier available, then $0.075/M tokens input, $0.30/M output
- Check: https://ai.google.dev/pricing

## Alternative: OpenAI Fallback
```javascript
// For redundancy, also support OpenAI
const openai = require('openai');
const openaiClient = new openai.OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function generateWithFallback(inputs, preferred = 'gemini') {
  if (preferred === 'gemini') {
    try {
      return await generateScript(inputs);
    } catch (e) {
      console.warn('Gemini failed, falling back to OpenAI...');
    }
  }
  // OpenAI fallback implementation...
}
```

---

*Created: 2026-03-08*
