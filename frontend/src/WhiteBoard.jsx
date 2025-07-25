import './WhiteBoard.css'
import { BsPencil } from "react-icons/bs";
import { LuEraser } from "react-icons/lu";
import { useEffect, useRef, useState } from "react";
import Output from './Output';

const WhiteBoard = () => {

    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [tool, setTool] = useState('pencil'); 
    const [writtenImage, setWrittenImage] = useState(null);
    
    useEffect(() => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        }, []);


    const startDrawing = (e) => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.beginPath();
        ctx.moveTo(
            e.nativeEvent.offsetX,
            e.nativeEvent.offsetY
        );
        setIsDrawing(true);
    };

    const draw = (e) => {
        if (!isDrawing) return;
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');

        if (tool === 'pencil') {
            ctx.strokeStyle = 'black';
            ctx.lineWidth = 2;
            ctx.lineTo(
                e.nativeEvent.offsetX,
                e.nativeEvent.offsetY
            );
            ctx.stroke();
        } else if (tool === 'eraser') {
            ctx.clearRect(
                e.nativeEvent.offsetX - 5,
                e.nativeEvent.offsetY - 5,
                30,
                30
            );
        }
    };

    const endDrawing = () => {
        setIsDrawing(false);
    };

    const handleReset = () => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    };

   const handleSubmit = () => {
    const canvas = canvasRef.current;
    const imageData = canvas.toDataURL("image/png");
    const base64Image = imageData.replace(/^data:image\/png;base64,/, '');

    console.log(base64Image)

    fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: base64Image }),
      })
        .then(res => res.json())
        .then(data => console.log('Server response:', data))
        .catch(err => console.error('Error:', err));
};


    return (
        <div className="white-board-container">
            <div>
                <div className='icons-container'>
                    <BsPencil
                        className='icons'
                        onClick={() => setTool('pencil')}
                    />
                    <LuEraser
                        className='icons'
                        onClick={() => setTool('eraser')}
                    />
                </div>

                <canvas
                    ref={canvasRef}
                    width={900}
                    height={500}
                    className="whiteboard-canvas"
                    onMouseDown={startDrawing}
                    onMouseMove={draw}
                    onMouseUp={endDrawing}
                    onMouseLeave={endDrawing}
                ></canvas>

                <div className='button-container'>
                    <button
                        className='reset-button'
                        onClick={handleReset}
                    >
                        Reset
                    </button>
                    <button className='submit-button' onClick={handleSubmit}>Submit</button>
                </div>
            </div>

            {
                <Output
                writtenImage={writtenImage}
                ></Output>
            }
        </div>
    );
};

export default WhiteBoard;
