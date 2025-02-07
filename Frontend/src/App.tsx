import React, { useState } from 'react';
import { Upload, PlayCircle, Map, AlertTriangle, BarChart3 } from 'lucide-react';
import axios from 'axios';

interface AudioRegion {
  name: string;
  poachingLevel: number;
  incidents: number;
}

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  
  // Mock data for demonstration
  const regions: AudioRegion[] = [
    { name: "Fire", poachingLevel: 75, incidents: 12 },
    { name: "Rain", poachingLevel: 45, incidents: 7 },
    { name: "Thunderstorm", poachingLevel: 90, incidents: 15 },
    { name: "Chainsaw", poachingLevel: 30, incidents: 4 }
  ];

  const handleFileChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file && file.type.startsWith('audio/')) {
      setSelectedFile(file);
      setIsUploading(true);
      
      const formData = new FormData();
      formData.append('file', file);

      try {
        // Upload the file to the server (without prediction)
        await axios.post('http://127.0.0.1:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setIsUploading(false);
      } catch (error) {
        console.error("Error during file upload:", error);
        setIsUploading(false);
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-green-700 text-white p-6">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <AlertTriangle size={24} />
            <h1 className="text-2xl font-bold">Audio Detection System</h1>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto p-6">
        {/* Upload Section */}
        <section className="mb-8">
          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="flex items-center justify-center w-full">
              <label className="w-full flex flex-col items-center px-4 py-6 bg-white rounded-lg border-2 border-dashed border-green-700 cursor-pointer hover:bg-green-50 transition-colors">
                <Upload className="w-12 h-12 text-green-700" />
                <span className="mt-2 text-base text-gray-600">
                  {selectedFile ? selectedFile.name : "Drop audio file or click to upload"}
                </span>
                <input
                  type="file"
                  className="hidden"
                  accept="audio/*"
                  onChange={handleFileChange}
                />
              </label>
            </div>
          </div>
        </section>

        {/* Analysis Dashboard */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Audio Visualization */}
          <section className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <PlayCircle className="mr-2" /> Audio Analysis
            </h2>
            <div className="h-48 bg-gray-100 rounded flex items-center justify-center">
              {isUploading ? (
                <div className="text-gray-500">Uploading audio...</div>
              ) : (
                <div className="text-gray-500">
                  {selectedFile ? "Audio waveform will appear here" : "Upload an audio file to begin"}
                </div>
              )}
            </div>
          </section>

          {/* Region Map */}
          <section className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <Map className="mr-2" /> Classes Overview
            </h2>
            <div className="h-48 bg-gray-100 rounded">
              <div className="p-4">
                {regions.map((region) => (
                  <div key={region.name} className="mb-2">
                    <div className="flex justify-between text-sm mb-1">
                      <span>{region.name}</span>
                      <span>{region.poachingLevel}% Presence</span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div
                        className="bg-red-600 h-2 rounded-full"
                        style={{ width: `${region.poachingLevel}%` }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </section>

          {/* Statistics */}
          <section className="bg-white rounded-lg shadow-md p-6 md:col-span-2">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <BarChart3 className="mr-2" /> Class Statistics
            </h2>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              {regions.map((region) => (
                <div
                  key={region.name}
                  className="p-4 rounded-lg bg-gray-50"
                >
                  <h3 className="font-medium text-gray-800">{region.name}</h3>
                  <p className="text-2xl font-bold text-green-700">{region.incidents}</p>
                  <p className="text-sm text-gray-500">Detected Incidents</p>
                </div>
              ))}
            </div>
          </section>
        </div>
      </main>
    </div>
  );
}

export default App;
