#!/usr/bin/env bash
# Install Rust & Cargo inside Render (User Home Directory)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$HOME/.cargo/bin:$PATH"

# Upgrade pip and install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
