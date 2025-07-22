
import './Output.css'
import { IoCloseOutline } from "react-icons/io5";
import { FaCheck } from "react-icons/fa6";
import { HiOutlineSpeakerWave } from "react-icons/hi2";
const Output = ({writtenImage}) => {
    return (
        <div className="Output-container-div">
            <div className="Output-container">
                    <p>Predicted Output</p>
                    <div> <HiOutlineSpeakerWave className='sound-icon' /></div>
                    <img className='output-image' src={writtenImage} alt="" />
                    
            </div>
            <div className='output-button-container'>
                <button className='incorrect-button'>Incorrect <IoCloseOutline className='wrong-icon'/></button>
                <button className='correct-button'>Correct <FaCheck className='right-icon'/></button>
            </div>
        </div>
    );
};

export default Output;