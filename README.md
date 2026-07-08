# AI Vision

AI-powered image analysis for Android using multiple state-of-the-art models.

## Features

- 🖼️ **Batch Image Analysis** - Process multiple images simultaneously with parallel processing
- 🤖 **Dynamic Model Sync** - Automatically fetches and syncs the latest available vision models natively from Pollinations API or your custom provider's endpoint
- 🎨 **Custom AI Providers** - Built-in support to optionally override the Base URL and intelligently sync models and analyze images with any OpenAI-compatible provider
- ✍️ **Custom Prompts** - Add your own prompts to tailor the analysis
- 🎨 **Material Design 3** - Modern, clean UI with dark/light theme support
- 📋 **Quick Copy** - One-tap copy results to clipboard
- ⏱️ **Real-time Timer** - Track analysis duration with live updates
- 🛑 **Stop Analysis** - Cancel ongoing analysis anytime
- 🔄 **State Preservation** - Resume analysis after app restart or configuration changes
- 💰 **Balance Checker** - Check Pollinations API balance directly from the settings dialog (hides automatically if using a custom Base URL)

## Available Models

The app natively and dynamically syncs all available vision models directly from the API on startup, ensuring you always have access to the latest state-of-the-art models without requiring an app update. By default, it natively syncs from the Pollinations AI API, but it will dynamically adapt to any custom provider you configure.

- **Custom Model:** You can always enter a custom model name manually via the "Custom Model" option in the selection menu.

## Configuration

### API Key & Base URL

The app requires an API key to function. You can seamlessly use the default Pollinations AI or any custom provider:

1. Open Settings (⚙️ icon)
2. **(Optional)** Enter a custom `Base URL` (e.g., `https://api.openai.com/v1/`) if you want to use a different AI provider.
3. Enter your API key securely.
4. Check your balance using the "Balance" button (Note: This button automatically hides if you are using a custom Base URL).

**Default API URL:** `https://gen.pollinations.ai/v1/`

### Model Sync

Models are fetched dynamically on startup. To manually sync all available models from the API:
1. Tap the model icon in the toolbar
2. Tap the "Sync" button
3. Synced models automatically persist across app restarts

## Usage

### Analyzing Images

1. Tap **"Select Image"** to choose from your gallery
2. Select single or multiple images (batch selection supported)
3. (Optional) Enter a custom prompt like "Describe in detail" or "What objects are visible?"
4. Tap **"Analyze"** to start
5. Tap **"Stop"** to cancel if needed
6. View results with markdown formatting
7. Tap the **copy icon** to copy results to clipboard

**Note:** Multiple images are processed in parallel for faster results. Each image result is clearly separated with headers.

### Changing Theme

1. Tap the **theme icon** in the toolbar
2. Switches between light and dark mode
3. Preference is saved automatically

## For Developers

### Tech Stack

- **Language:** Kotlin
- **Min SDK:** 24 (Android 7.0)
- **Target SDK:** 34 (Android 14)
- **Architecture:** Single Activity with coroutines for async operations
- **Key Libraries:**
  - Material Design 3 (UI components)
  - OkHttp (HTTP client)
  - Kotlin Coroutines (async/parallel processing)
  - Markwon (Markdown rendering)
  - ViewBinding (view access)

### Build Commands

```bash
# Debug build
./gradlew assembleDebug

# Release build (signed)
./gradlew assembleRelease

# Install on connected device
./gradlew installDebug
```

### CI/CD

GitHub Actions automatically:
- Builds release APK on push to main branch
- Auto-increments version tags
- Creates GitHub releases with APK artifacts
- Uploads build artifacts

Workflow file: `.github/workflows/build.yml`

## Permissions

- `INTERNET` - Required for API calls
- `READ_MEDIA_IMAGES` - Gallery access on Android 13+
- `READ_EXTERNAL_STORAGE` - Gallery access on Android 12 and below

## License

Open source. Use, modify, and distribute freely.
