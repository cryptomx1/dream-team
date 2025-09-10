# Dream Team - AI Consensus System

A distributed AI consensus system built with Flask that enables multiple AI agents to collaborate and reach consensus through voting mechanisms.

## Architecture

- **middleware.py**: Central Flask API for message handling and coordination
- **voting_daemon.py**: Monitors messages and calculates consensus based on votes  
- **responder.py**: AI response generation with voting integration
- **chatbot.py**: Voice-activated interface with speech recognition and TTS
- **voice_core.py**: Local language model integration
- Various test utilities for voice and TTS functionality

## Vercel Serverless Deployment

This project is configured for serverless deployment on Vercel using Python 3.11 runtime.

### Deployment Setup

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel --prod
   ```

### Configuration Files

- **vercel.json**: Configures Python 3.11 runtime and routes
- **api/index.py**: Serverless function wrapper using vercel-wsgi
- **requirements.txt**: Minimal dependencies (Flask, vercel-wsgi, requests)

### API Endpoints

The following endpoints are available both locally and on Vercel:

- `POST /post_message`: Add a message to the system
- `GET /get_messages`: Retrieve all messages
- `POST /clear_messages`: Clear all messages

### Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run locally**:
   ```bash
   python middleware.py
   ```

3. **Test endpoints**:
   ```bash
   # Test GET endpoint
   curl http://localhost:5000/get_messages
   
   # Test POST endpoint
   curl -X POST http://localhost:5000/post_message \
        -H "Content-Type: application/json" \
        -d '{"from": "TestUser", "content": "Hello World"}'
   
   # Test clear endpoint
   curl -X POST http://localhost:5000/clear_messages
   ```

### Vercel Testing

Once deployed, test your Vercel deployment:

```bash
# Replace YOUR_DEPLOYMENT_URL with your actual Vercel URL
export VERCEL_URL="https://your-deployment.vercel.app"

# Test GET endpoint
curl $VERCEL_URL/get_messages

# Test POST endpoint  
curl -X POST $VERCEL_URL/post_message \
     -H "Content-Type: application/json" \
     -d '{"from": "TestUser", "content": "Hello from Vercel"}'

# Test clear endpoint
curl -X POST $VERCEL_URL/clear_messages
```

### Health Check Workflow

The project includes an optional CI workflow (`vercel-health.yml`) that automatically tests the deployed endpoints.

**To enable the health check workflow:**

1. Go to your GitHub repository Settings > Secrets and variables > Actions
2. Add a repository variable named `VERCEL_BASE_URL` 
3. Set the value to your Vercel deployment URL (e.g., `https://your-deployment.vercel.app`)

The workflow will then:
- Run on pushes to main/deploy branches
- Run every 6 hours as a scheduled check  
- Test all three API endpoints
- Report failures for monitoring

### Dependencies

**Core Requirements (requirements.txt):**
- Flask==2.3.3: Web framework
- requests==2.31.0: HTTP client for inter-service communication

Note: The vercel-wsgi package is not required for modern Vercel Python runtime, which natively supports WSGI applications.

**Additional Local Dependencies (not included in Vercel deployment):**
- speech_recognition: Voice input processing
- pyttsx3: Text-to-speech synthesis  
- transformers: Language model integration
- torch: Machine learning framework

Note: Heavy dependencies like audio libraries and ML models are intentionally excluded from the Vercel deployment to keep it lightweight and fast.

## Usage

### Basic Message Flow

1. POST a message via `/post_message`
2. AI responders process and vote
3. Voting daemon calculates consensus
4. Retrieve results via `/get_messages`
5. Clear state via `/clear_messages` for next interaction

### Integration with AI Components

The serverless API can be used by:
- External chatbots and AI services
- Web frontends and mobile apps
- Other microservices in the AI consensus workflow
- Monitoring and analytics tools

## Contributing

When making changes:
1. Preserve the existing Flask app structure in `middleware.py`
2. Keep Vercel deployment lightweight (avoid heavy dependencies)
3. Test both local and serverless deployments
4. Update health checks if adding new endpoints