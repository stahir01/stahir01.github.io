// Keep entire conversation in this array
let conversation = [
    { role: "assistant", content: "Hello! I'm Burny's AI. Ask me anything about his experience!" }
  ];
  
  document.addEventListener("DOMContentLoaded", () => {
    // Show initial greeting
    renderConversation();
  });
  
  // Toggle chatbot popup
  function toggleChatbot() {
    const popup = document.getElementById("chatbot-popup");
    popup.style.display = (popup.style.display === "none" || !popup.style.display) ? "flex" : "none";
  }
  
  // Render conversation in #chatbot-messages
  function renderConversation() {
    const messagesDiv = document.getElementById("chatbot-messages");
    messagesDiv.innerHTML = ""; // Clear existing
  
    conversation.forEach(msg => {
      const div = document.createElement("div");
      div.classList.add("message");
      div.classList.add(msg.role === "user" ? "user" : "bot");
      div.textContent = msg.content;
      messagesDiv.appendChild(div);
    });
  
    // Auto-scroll to bottom
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  }
  
  // Send user message to backend
  async function sendMessage() {
    const input = document.getElementById("user-message");
    const userText = input.value.trim();
    if (!userText) return;
  
    // Add user message to conversation array
    conversation.push({ role: "user", content: userText });
    input.value = "";
  
    // Re-render conversation
    renderConversation();
  
    try {
      // POST entire conversation to the backend
      const response = await fetch("http://127.0.0.1:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ conversation })
      });
  
      if (!response.ok) {
        throw new Error("Network response was not OK");
      }
  
      const data = await response.json();
      // data should have { role: "assistant", content: "..." }
  
      // Add new bot message
      conversation.push({
        role: data.role || "assistant",
        content: data.content || "Sorry, I can't respond at the moment."
      });
  
      renderConversation();
    } catch (error) {
      console.error("Error sending message:", error);
      conversation.push({
        role: "assistant",
        content: "Error: Unable to connect to the server."
      });
      renderConversation();
    }
  }
  